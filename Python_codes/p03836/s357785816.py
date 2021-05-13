import sys


def input(): return sys.stdin.readline().strip()


def resolve():
    s1, s2, t1, t2 = map(int, input().split())
    l = []
    x = t1 - s1
    y = t2 - s2
    ans='R'*x+'U'*y+'L'*x+'D'*y
    ans+='D'+'R'*(x+1)+'U'*(y+1)+'L'
    ans+='U'+'L'*(x+1)+'D'*(y+1)+'R'
    print(ans)
resolve()