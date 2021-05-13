n = int(input())
L = []
for i in range(3):
    L.append(input())

cnt = 0
for i in range(n):
    s = set((L[0][i],L[1][i],L[2][i]))
    cnt += len(s)-1
print(cnt)
