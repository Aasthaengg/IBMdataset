n = int(input())
ratio_array = [tuple(map(int, input().split())) for _ in range(n)]

votes_numｓ = (1, 1)

for x, y in ratio_array:
    t, a = votes_numｓ
    m = max((t+x-1)//x, (a+y-1)//y)
    votes_numｓ = (m*x, m*y)

print(sum(votes_numｓ))