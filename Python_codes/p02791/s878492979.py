n = int(input())
p = list(map(int, input().split()))
mnm = 2 * 10**5
ans = 0
for i in p:
    if i <= mnm:
        mnm = i
        ans += 1
print(ans)