n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
before = -100
for i in a:
    i -= 1
    if i == before + 1:
        ans += c[before]
    before = i
    ans += b[i]
print(ans)