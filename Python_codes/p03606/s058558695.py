n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
sum1 = 0
for i in l:
  sum1 += i[1] - (i[0] - 1)
print(sum1)