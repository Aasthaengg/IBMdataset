import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

s = S()
ans = 0
temp = 0
for i in s:
    if i in 'ACGT':
        temp += 1
    else:
        temp = 0
    ans = max(ans,temp)
print(ans)