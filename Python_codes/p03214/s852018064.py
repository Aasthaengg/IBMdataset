n = int(input())
numlist = list(map(int, input().split()))
cal = 0
for i in numlist:
  cal = cal + i
ave = cal / (n)
dummy = abs(numlist[0]-ave)
index = 0
count = 0
for j in numlist:
  kyori = abs(j-ave)
  if dummy > kyori:
    dummy = kyori
    index = count
  count = count + 1 
print(index)
