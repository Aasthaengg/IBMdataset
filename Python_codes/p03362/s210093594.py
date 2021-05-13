import collections

# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N = int(input())
    tmplist = []
    #restlist = []
    for i in range(2, 55556):
        tmp = prime_factorize(i)
        if len(tmp) == 1:
            tmplist.append(i)
            #restlist.append(i%5)
    
    #count = collections.Counter(restlist)
    #print(count)
    ans = []
    for tmp in tmplist:
        if tmp%5 == 1:
            ans.append(tmp)
        if len(ans) == N:
            print(*ans)
            return

if __name__ == "__main__":
    main()
