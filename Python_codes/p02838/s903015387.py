def main():
    n = int(input())
    A=[int(i) for i in input().split()]
    MOD = 10**9 + 7
    t = 0
    k = max(A)
    while k>0:
        k=k//2
        t+=1

    bisu = [0]*(t+1)
    zerobi = [0]*(t+1)
    res = 0
    for i in range(n):
        for j in range(t+1):
            if A[i]&(1<<j):
                bisu[j]+=1

    for i in range(t+1):
        res = res + (bisu[i]*(n-bisu[i])*(2**i))%MOD
    print(res%MOD)

if __name__ == '__main__':
    main()
