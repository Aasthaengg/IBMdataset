import sys
from itertools import combinations_with_replacement,product
def input(): return sys.stdin.readline().rstrip()
 
def main():
    n=int(input())
    li=[]
    for i in range(n):
        lia=[]
        A=int(input())
        for j in range(A):

            x,y=map(int, input().split())
            x-=1
            lia.append([x,y])
        li.append(lia)
    ans = 0
    for k in list(product([0,1],repeat=n)):
        if ans >= sum(k):
            continue
        kt = list(k)
        for y in range(n):
            if kt[y]==1:
                for g in li[y]:
                    if g[1] != kt[g[0]]:
                        break
                else:
                    continue
                break
        else:
            ans = sum(k)
            
    print(ans)



if __name__=='__main__':
    main()