N,D = map(int, input().split())
count = 0
i = 0
while i < N:
  i += 2*D+1
  count +=1
print(count)
