import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()

ans = 0
for i in range(0,N,2):
    if a[i] % 2 == 1:
        ans += 1

print(ans)