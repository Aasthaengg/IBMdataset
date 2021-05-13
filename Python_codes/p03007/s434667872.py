import sys
input = sys.stdin.buffer.readline
from operator import itemgetter

def main():
    N = int(input())
    a = list(map(int,input().split()))
    posi,nega = [],[]
    for num in a:
        if num >= 0:
            posi.append(num)
        else:
            nega.append(num)
    
    posi.sort()
    nega.sort(reverse=True)
    ans = []
    if len(posi) == 0:
        a = nega[0]
        for i in range(N-1):
            ans.append((a,nega[i+1]))
            a -= nega[i+1]
    elif len(nega) == 0:
        if len(posi) == 2:
            ans.append((max(posi),min(posi)))
        else:
            a = posi[0]
            for i in range(N-2):
                ans.append((a,posi[i+1]))
                a -= posi[i+1]
            ans.append((posi[-1],a))
    else:
        pl,nl = len(posi),len(nega)
        a = posi[0]
        for i in range(pl-1):
            ans.append((nega[0],posi[i+1]))
            nega[0] -= posi[i+1]
        for i in range(nl):
            ans.append((a,nega[i]))
            a -= nega[i]
            
    print(ans[-1][0]-ans[-1][1])
    for x,y in ans:
        print(x,y)

if __name__ == "__main__":
    main()
