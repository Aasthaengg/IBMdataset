n = int(input())
l = sorted([list(map(int, input().split())) for i in range(n)])[::-1]
ans = l[0][0] + l[0][1]
print(ans)