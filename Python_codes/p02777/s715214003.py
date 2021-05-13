m,n = map(str,input().split())
a,b = map(int,input().split())

f = str(input())

if f == m:
  a = a -1
else:
  b = b -1 

print(str(a) + " " + str(b))