import sys
sys.setrecursionlimit(10**7)
def dfs(s,m):
    if len(s)==N:
        li.append(s)
        return
    for c in range(97,ord(m)+2):
        dfs(s+chr(c),max(m,chr(c)))

N=int(input())
li=[]
li.sort()
dfs('a','a')
print(*li,sep='\n')