N = int(input())
a = [0 for _ in range(N + 10)]

for i in range(1, N + 5):
    temp = i
    while(temp <= N):
        a[temp] += 1
        temp += i
ans = 0
for i in range(1, N + 1, 2):
    if a[i] == 8:  ans += 1
print(ans)