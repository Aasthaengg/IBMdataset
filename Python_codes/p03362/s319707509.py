from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    p=primes(55555)
    q=[x for x in p if x%5==1]
    print(*q[:n])

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,n+1):
        if i*i>n:
            break
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

if __name__=="__main__":
    main()