import sys
def input(): return sys.stdin.readline().strip()
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
l=sorted(l,key=lambda x: x[0],reverse=True)
print(sum(l[0]))