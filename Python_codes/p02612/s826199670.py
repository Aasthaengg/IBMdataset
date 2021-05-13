N = int(input().rstrip())
num = 0

if N%1000 == 0:
  num = N//1000
else:
  num = N//1000 + 1
change = num*1000 - N
print(change)