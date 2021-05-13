a, b, c = map(int, input().split())
k = int(input())

ABC = [a, b, c]
sort_ACB = sorted(ABC)
MAX = sort_ACB[-1]
sum_ABC = sum(ABC) - MAX

for _ in range(k):
  MAX*=2
print(sum_ABC + MAX)