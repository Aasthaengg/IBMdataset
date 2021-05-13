N = int(input())
p = list(map(int, input().split()))
lst = [i for i in range(1, N + 1)]
count = 0

for i in range(N):
    if p[i] != lst[i]:
        count += 1

if count < 3:
    print("YES")
else:
    print("NO")