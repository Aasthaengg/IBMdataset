N = int(input())
count = 0
for up_from_0 in range(1,N):
  down_from_N = N-up_from_0
  if up_from_0 < down_from_N :
    count += 1
print(count)