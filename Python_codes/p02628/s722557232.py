n,k = map(int, input().split())
N = list(map(int,input().split()))
N.sort(key = int)
sum = 0

for i in range(k):
  sum = sum + N[i]

print(sum)