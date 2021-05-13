n = int(input())
people = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in people:
    ans += i[1] - i[0] + 1
print(ans)