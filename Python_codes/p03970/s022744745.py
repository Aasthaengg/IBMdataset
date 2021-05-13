import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    l='CODEFESTIVAL2016'
    s=str(input())
    ls=len(s)
    cnt=0
    for i in range(ls):
        if s[i]!=l[i]: cnt+=1
    print(cnt)
    
resolve()