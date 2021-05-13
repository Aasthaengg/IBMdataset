_ = input()
K = int(input())
X = [int(i) for i in input().split()]

s = 0
for x in X:
  l = min(x, K - x)
  s += l * 2
print(s)