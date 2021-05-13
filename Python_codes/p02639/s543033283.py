n = list(map(int, input().split()))
result = 0
for i in range(len(n)):
  if n[i] == 0:
    print(i+1)