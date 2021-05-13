

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=[]
    for i in range(3):
        A.append(input())
        
    ans=0
    for i in range(N):
        t=set([])
        for j in range(3):
            t.add(A[j][i])
        ans+=len(t)-1
        
    print(ans)
        

main()
