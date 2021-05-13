n = int(input())
lis_d = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
  if lis_d[i][0] == lis_d[i][1] and lis_d[i+1][0] == lis_d[i+1][1] and lis_d[i+2][0] == lis_d[i+2][1]:
    print("Yes")
    exit()

print("No")