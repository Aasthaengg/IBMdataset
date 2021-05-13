N = int(input())
t = []
index = {}
for n in range(N):
    si, ti = input().split()
    ti = int(ti)
    index[si] = n
    t.append(ti)

X = input()

ans = 0
for i in range(index[X]+1, N):
    ans += t[i]

print(ans)