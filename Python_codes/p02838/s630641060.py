from collections import defaultdict
def main2():
    ketaone = [0]*61
    MOD = 10**9 + 7
    n = int(input())
    A=[int(i) for i in input().split()]

    for i in A:
        for j in range(61):
            if i&(1<<j):
                ketaone[j]+=1
    res = 0

    for i in range(61):
        res = res + (ketaone[i]*(n-ketaone[i])*(2**i))%MOD
        res%=MOD
    print(res)


def main1():
    n = int(input())
    lis = [[] for _ in range(n)]
    for i in range(n):
        a = int(input())
        for j in range(a):
            lis[i].append(list(map(int, input().split())))
    res = 0

    for i in range(1<<n):
        f = True
        uso=set()
        syo=set()
        tmp=0
        for j in range(n):
            if(i&(1<<j)):
                tmp+=1
                for k in lis[j]:
                    if (i&(1<<(k[0]-1))) and k[1]==0:
                        f=False
                    if k[1]==1 and not (i&(1<<k[0]-1)):
                        f=False
        if f:
            res = max(res,tmp)
    print(res)


if __name__ == '__main__':
    main2()
