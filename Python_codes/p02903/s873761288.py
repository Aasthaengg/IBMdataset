import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,A,B=MI()
    if H!=1 and W!=1:
        s=[[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i<B and j<A:
                    s[i][j]=1
                elif i>=B and j>=A:
                    s[i][j]=1
                else:
                    pass
                
        for i in range(H):
            print(''.join(map(str, s[i])))
    else:
        if H==1:
            ans=([1]*A)+([0]*(W-A))
            print(''.join(map(str,ans)))
        else:
            for i in range(H):
                if i<B:
                    print(1)
                else:
                    print(0)
            

main()
