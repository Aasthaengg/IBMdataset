import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    
    llst = [0 for _ in range(len(s)+2)]
    rlst = [0 for _ in range(len(s)+2)]

    for i in range(1, len(s)+1):
        if s[i-1] == "<":
            llst[i] = llst[i-1] + 1
    
    for i in range(len(s)-1, -1, -1):
        if s[i] == ">":
            rlst[i] = rlst[i+1] + 1
    
    ans = 0

    for i in range(len(s)+1):
        ans += max(llst[i], rlst[i])

    print(ans)

main()
