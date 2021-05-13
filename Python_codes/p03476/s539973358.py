def sieve(n):
    is_prime =[True for i in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i+i,n,i):
                is_prime[j] = False
    c = [0 for i in range(n+1)]
    for i in range(3,n+1,2):
        if is_prime[i] and is_prime[(i+1)//2]:
            c[i] = 1
    for i in range(n):
        c[i+1] += c[i]
    return c

def solve(l,r,c):
    return c[r]-c[l-1]



if __name__ == '__main__':
    q = int(input())
    c = sieve(100000)
    for i in range(q):
        l,r = map(int,input().split())
        print(solve(l,r,c))