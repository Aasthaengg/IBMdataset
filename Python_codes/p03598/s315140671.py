N = int(input())
K = int(input())
x = map(int, input().split())
sum_of_x = 0
for i in x:
  sum_of_x += min(i - 0, abs(i - K))
print(2 * sum_of_x)