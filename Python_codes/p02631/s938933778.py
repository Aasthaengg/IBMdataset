N = int(input())
a = list(map(int, input().split()))
s_a = a[0]
for i in range(1, len(a)):
    s_a = s_a^a[i]

ans = []
for i in range(len(a)):
    ans.append(s_a^a[i])
print(*ans)