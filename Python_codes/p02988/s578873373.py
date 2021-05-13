n = int(input())
L = list(map(int, input().split()))
count = 0
for i in range(1,n-1):
  if (L[i-1] < L[i] and L[i] < L[i+1]) or (L[i-1] > L[i] and L[i] > L[i+1]):
    count += 1
print(count)    