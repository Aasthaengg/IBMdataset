import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
s = S()
ans = 0
for i in range(1000):
    num = str(i).zfill(3)
    if s.find(num[0]) == -1:
        continue
    s1 = s[s.find(num[0])+1:]
    if s1.find(num[1]) == -1:
        continue
    s2 = s1[s1.find(num[1])+1:]
    if s2.find(num[2]) == -1:
        continue
    ans+=1
print(ans)

