a,b,c = map(int,input().split())
k = int(input())
for i in range(k):
         if b <= a:
                  b *= 2
                  k -= 1
for i in range(k):
         if c <= b:
                  c *= 2
if a < b and b < c:
         print ("Yes")
else:
         print("No")
         

