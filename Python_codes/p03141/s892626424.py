N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
sum_B = sum([b for a, b in AB])
ans = sum(sorted([a+b for a, b in AB], reverse=True)[::2]) - sum_B
print(ans)