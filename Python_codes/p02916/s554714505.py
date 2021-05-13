n = int(input())
ans = 0
p = -999
a = [i - 1 for i in map(int, input().split())]
b = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in a:
    ans += b[i]
    if i == p + 1:
        ans += c[p]
    p = i
print(ans)