import sys,math
input = sys.stdin.readline

a_max=0
b = []
N,H = map(int,input().split())
for i in range(N):
    an,bn = map(int,input().split())
    b.append(bn)
    a_max = max(a_max,an)

b = sorted([ bn for bn in b if bn>=a_max])
cnt = 0
for i in range(len(b)):
    H -= b.pop()
    cnt += 1
    if H <=0:
        print(cnt)
        exit()

cnt += math.ceil(H/a_max)
print(cnt)