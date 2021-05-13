N = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

candies = []
for n in range(N):
  c1 = sum(row1[0:n + 1])
  c2 = sum(row2[n : N])
  candies.append(c1 + c2)

print(max(candies))