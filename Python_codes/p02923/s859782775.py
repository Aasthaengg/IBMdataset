import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
H = LI()

ans = 0
a = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        a += 1
    else:
        ans = max(ans,a)
        a = 0
ans = max(ans,a)
print(ans)
