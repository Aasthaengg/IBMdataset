#def solver():
inputdata=input().split()
n=int(inputdata[0])
k=int(inputdata[1])
pointer=1
while pointer +k <= n:
  pointer = pointer +1

if n < k:
  print("0")
else:
  print(pointer)

