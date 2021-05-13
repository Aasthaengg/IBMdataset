array = list(map(int,input().split()))
count = 0
for i in range(5):
  count += 1
  if array[i] == 0:
    print(count)
