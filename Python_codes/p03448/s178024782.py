a=int(input())#500
b=int(input())#100
c=int(input())#50
n=int(input())
co=0
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      go=500*i+100*j+50*k
      if go==n:
        co+=1
print(co)