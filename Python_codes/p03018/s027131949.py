import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    s=input()
    s2=list(s.replace('BC','D'))
    N=len(s2)
    ans=0
    c=0
    for i in range(N):
        if s2[i]=='A':
            c+=1
        elif c!=0 and s2[i]=='D':
            ans+=c
        else:
            c=0
    print(ans)

if __name__ == '__main__':
    main()
