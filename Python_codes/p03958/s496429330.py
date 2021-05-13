from collections import deque
k,t = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
a = deque(a)
length = len(a)
if length ==1:
    print(sum(a)-1)
    exit()
while length > 1:
    mx = a.pop()
    mn = a.popleft()
    mx -= 1
    mn -= 1
    if mx != 0:
        a.append(mx)
    else:
        length -=1
    if mn != 0:
        a.appendleft(mn)
    else:
        length-=1    
print(max(sum(a)-1,0))     
