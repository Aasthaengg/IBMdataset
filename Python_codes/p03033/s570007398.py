import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    N,Q = list(map(int,input().split()))

    road = []
    x_list = []

    for i in range(N):
        s,t,x = list(map(int,input().split()))
        road.append([0,s-x,x])
        road.append([1,t-x,x])

    for i in range(Q):
        road.append([2,int(input()),i])

    from collections import defaultdict

    counter = defaultdict(int)
    counter[10**27] = 1
    ans = [0]*Q

    road.sort(key=lambda x:x[0])
    road.sort(key=lambda x:x[1])

    q = [10**27]

    from heapq import heappop,heappush

    for id,_,x in road:
        if id==0:
            heappush(q,x)
            counter[x]+=1
        elif id==1:
            counter[x]-=1
        else:
            while counter[q[0]]==0:
                heappop(q)
            #print(q)
            if q[0]<10**27:
                ans[x] = q[0]
            else:
                ans[x] = -1
    print("\n".join(map(str,ans)))

if __name__ == '__main__':
    main()

