h,w = map(int,input().split())

a1 = ["#"]*(w+2)
x = [0]*h
for i in range(0,h):
  x[i] = input().split()

a1 = ''.join(a1)

print(a1)
for i in range(0,h):
  x[i] = ''.join(x[i])
  print("#"+x[i]+"#")
print(a1)