h,w = map(int, input().split())
a = [input() for i in range(h)]
abc = [0]*26
import heapq

for i in range(h):
  for j in range(w):
    abc[ord(a[i][j])-ord("a")]+=1

heap=[]
heapq.heapify(heap)
for i in range(26):
  if abc[i]!=0:
    heapq.heappush(heap, -1*abc[i])
    
num4 = (h//2)*(w//2)
num2 = 0
if h%2==1:
  num2+=w//2
if w%2==1:
  num2+=h//2
    
while num4>0:
  temp=-1*heapq.heappop(heap)
  if temp>=4:
    if temp > 4:
      heapq.heappush(heap, -1*(temp-4))
    num4-=1
  else:
    print("No")
    quit()
    
while num2>0:
  temp=-1*heapq.heappop(heap)
  if temp>=2:
    if temp > 2:
      heapq.heappush(heap, -1*(temp-2))
    num2-=1
  else:
    print("No")
    quit()  
print("Yes")
