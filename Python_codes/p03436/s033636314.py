# coding: utf-8
# Your code here!
from collections import deque
h,w = map(int,input().split())
s = []
bcnt = 0
for i in range(h):
    ss = list(input())
    bcnt += ss.count("#")
    s.append(ss)
def next(x,y,h,w):
    global s
    ret = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    ans = []
    for i in ret:
        if i[0] >= 0 and i[0] < w and i[1] >= 0 and i[1] < h:
            if s[i[1]][i[0]] == ".":
                ans.append(i)
    return ans

queue = deque([(0,next(0,0,h,w))])
#print(queue)
visited = {(0,0):0}
while queue != deque([]):
    label = queue.popleft()
    #print(label)
    for i in label[1]:
        if not i in visited:
            visited[i] = label[0]+1
            queue.append((label[0]+1,next(i[0],i[1],h,w)))
if (w-1,h-1) in visited:
    print(h*w-bcnt-visited[(w-1,h-1)]-1)
else:
    print(-1)