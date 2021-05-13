import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=input()
    ans=0
    if int(n)%10!=0:
        for i in range(len(n)):
            ans+=int(n[i])
    else:
        ans=10
    print(ans)
resolve()