
n = int(input())
t, a = [0] * n, [0] * n
for i in range(n):
    t[i], a[i] = map(int, input().split())
ans = a[0] + t[0]
j_pre = 1
for i in range(1, n):
    j = max(-(-(t[i - 1] * j_pre) // t[i]), -(-(a[i - 1] * j_pre) // a[i]) )
    ans = (t[i] + a[i]) * j
    j_pre = j
    #print(t[i] * j, a[i] * j)
    #print(ans)

print(ans)