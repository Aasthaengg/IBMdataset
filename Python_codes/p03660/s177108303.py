#フェネックバーサス　スヌーく
n=int(input())
tree_list={i:[] for i  in range(1,n+1)}
for i  in range(n-1):
    a,b=map(int,input().split())
    tree_list[a].append(b)
    tree_list[b].append(a)
painted=[False for i in range(n+1)]
painted[1]="black"
painted[n]="white"
from collections import deque
d_white=deque()
e_white=deque()

d_black=deque()
e_black=deque()

d_black.append(1)
d_white.append(n)

while(d_black or d_white):
    for some in d_black:
        for point in tree_list[some]:
            if painted[point]==False:
                painted[point]="black"
                e_black.append(point)
    d_black=e_black
    e_black=deque()
    
    for some in d_white:
        for point in tree_list[some]:
            if painted[point]==False:
                painted[point]="white"
                e_white.append(point)
    d_white=e_white
    e_white=deque()
sunke=0
fennec=0
for i in range(1,n+1):
  if painted[i]=="white":
    sunke+=1
  elif painted[i]=="black":
    fennec+=1
if fennec>sunke:
  print("Fennec")
else:
  print("Snuke")