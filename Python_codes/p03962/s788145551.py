l = map(int,input().split())

li = sorted(l)

a = li[0] 
b = li[1] 
c = li[2] 

if a == b == c:
    print(1)
elif a == b or b == c:
          print(2)
else:
      print(3)
    