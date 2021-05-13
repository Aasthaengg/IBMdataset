

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    S=input()
    bk=S.count("#")
    ans=N-bk
    w=0
    for i in range(N):#i番目まで白，i+1以降黒
        if S[i]=="#":
            bk-=1
        else:
            w+=1
        temp=(i+1-w)+(N-i-1-bk)
        ans=min(ans,temp)
    print(ans)
        

main()
