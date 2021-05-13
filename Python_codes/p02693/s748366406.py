k = int(input())
a,b = map(int,input().split())

for i in range(b//k+1):
  if i*k >= a and i*k <= b:
    print("OK")
    exit()
print("NG")
  
