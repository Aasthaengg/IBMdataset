A500 = int(input())
B100 = int(input())
C50 = int(input())
X = int(input())

c = 0
for i in range(A500+1):
  for j in range(B100+1):
    for k in range(C50+1):
      if X == i*500 + j* 100 + k*50:
        c+=1
print(c)
