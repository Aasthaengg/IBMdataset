import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    ans=0
    s=input()
    ans+=s.count('+')
    ans-=s.count('-')
    print(ans)
resolve()