def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    S=S.replace("BC","D")
    S+="Z"
    N=len(S)
    ans=0
    cnta=0

    
    for i in range(N):
        if S[i]=="D":
            ans+=cnta
        elif S[i]=="A":
            cnta+=1
        else:
            cnta=0
                
    print(ans)
            

main()
