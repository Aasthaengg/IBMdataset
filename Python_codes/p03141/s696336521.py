N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
D = [[i, abs(a+b)] for i, (a, b) in enumerate(AB)]
D.sort(key=lambda x:x[1], reverse=True)
ta = [0, 0]
for j, (i, d) in enumerate(D):
  ta[j%2]+=AB[i][j%2]
print(ta[0]-ta[1])