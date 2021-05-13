n = int(input())
ns = sorted(list(map(int, input().split())))
cnt = 0
cum = [0]
for i in ns:
    cum.append(i + cum[-1])
for i in range(n):
    if cum[i] * 2 >= ns[i]:
        cnt += 1
    else:
        cnt = 0
print(cnt+1)