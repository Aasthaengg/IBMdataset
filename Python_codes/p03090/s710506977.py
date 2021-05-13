import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    t=0
    if N%2==0:
        t=1+N
    else:
        t=N
        
    ans=[]
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i+j!=t:
                ans.append([i,j])
    print(len(ans))
    for i in range(len(ans)):
        print(' '.join(map(str, ans[i])))
    


main()
