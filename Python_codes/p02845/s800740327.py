n = int(input())
a = list(map(int, input().split()))

c = [0, 0, 0]
ans = 1
for i in range(n):
    count = 0
    for j in range(3):
        if a[i] == c[j]:
            if count == 0:
                c[j] += 1
            count += 1
    ans = ans * count % 1000000007
print(ans)