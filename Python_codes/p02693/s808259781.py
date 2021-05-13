a = int(input())
list=list(map(int,input().split()))

b=list[0]//a
c=list[1]//a

if list[0]%a==0:
	print("OK")

elif c-b>=1:
	print("OK")

else:
  print("NG")
