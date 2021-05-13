N = int(input())
num = 0
for i in range(6):
  if N >= 10**i and N < 10**(i+1):
    keta = i+1
if keta == 1:
  num = N
elif keta == 2:
  num = 9
elif keta == 3:
  num = 9 + N - 99
elif keta == 4:
  num = 909
elif keta == 5:
  num = 909 + N -9999
else:
  num = 90909
print(num)