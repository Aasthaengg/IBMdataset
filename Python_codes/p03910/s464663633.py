N = int(input())

s = 0
ans = []
for i in range(1, N + 1):
    s += i
    if s >= N:
        for n in range(i, 0, -1):
            if N - n >= 0:
                ans.append(n)
                N -= n
        break

for i in ans:
    print(i)
