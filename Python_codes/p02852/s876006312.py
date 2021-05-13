n, m = map(int, input().split())
n += 1
s = input()
dst = [float("inf")]*n
dst[-1] = 0
m_last = n-1

for i in reversed(range(n-1)):
    if s[i] == "1":
        continue
    for j in reversed(range(min(m_last+1, i+m+1))):
        # print(i, j)
        if s[j] == "0":
            dst[i] = dst[j]+1
            m_last = j
            break

    if dst[i] == float("inf"):
        print(-1)
        exit()

# print(dst)
last_idx = 0
last_num = dst[0]
ans = []
for i in range(1, n):
    if dst[i] != float("inf") and dst[i] != last_num:
        ans.append(i - last_idx)
        last_num = dst[i]
        last_idx = i

print(*ans)

