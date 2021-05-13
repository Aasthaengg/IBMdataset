N = int(input())
Y = int(N/1.08)
a = Y
b = Y+1
if int(a*1.08) == N:
  print(a)
elif int(b*1.08) == N:
  print(b)
else:
  print(':(')
