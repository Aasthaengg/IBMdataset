D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [0 for i in range(26)]
for i in range(1, D+1):
  inc = [s[i-1][j] - c[j]*(i-t[j-1])*(i+1-t[j-1])//2 for j in range(26)]
  max_index = inc.index(max(inc))
  t[max_index] = i
  print(max_index+1)