import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W=MI()
    N=I()
    a=LI()
    ans=[[0]*W for _ in range(H)]
    num=0
    
    for k in range(H*W):
        i=k//W
        j=k%W
        if i%2==1:
            j=W-1-j
        if a[num]==0:
            num+=1
        ans[i][j]=num+1
        a[num]-=1
        
    for i in range(H):
        print(' '.join(map(str, ans[i])))
            
        
        

main()
