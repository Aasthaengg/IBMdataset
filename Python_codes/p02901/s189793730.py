

def main():
    n,m=map(int,input().split())

    L=2**n

    cost=[0]+[10**8 for i in range(L-1)]

    for _ in range(m):
        a,b = map(int,input().split())

        c = sum(map(lambda x:2**(int(x)-1), input().split()))
        for i in range(L):
            q = c|i
            cost[q] = min(cost[q], cost[i]+a)
    print(cost[L-1] if cost[L-1]<10**8 else -1)

if __name__ == '__main__':
    main()
