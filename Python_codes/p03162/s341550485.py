N = int(input())
day = [list(map(int, input().split())) for i in range(N)]

happiness = [[0,0,0] for i in range(N)]

happiness[0] = day[0]

for i in range(1, N):
  happiness[i][0] = day[i][0] + max(happiness[i-1][1], happiness[i-1][2])
  happiness[i][1] = day[i][1] + max(happiness[i-1][0], happiness[i-1][2])
  happiness[i][2] = day[i][2] + max(happiness[i-1][0], happiness[i-1][1])

print(max(happiness[N-1][0], happiness[N-1][1], happiness[N-1][2]))
