n = int(input())

k = 0
for i in range(10**3):
    if i * (i-1) // 2 == n:
        k = i
        break
else:
    print("No")
    exit()

ans = [[] for _ in range(k)]
cnt = 1
for i in range(k):
    for j in range(i+1, k):
        ans[i].append(cnt)
        ans[j].append(cnt)
        cnt += 1

print("Yes")
print(k)
for i in range(k):
    print(k-1, *ans[i])
