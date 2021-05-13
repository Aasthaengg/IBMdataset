from collections import deque
n=int(input())
a=list(map(int,input().split()))

even=deque()
odd=deque()

for i in range(n):
    if i%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])

ans=[]
while(len(odd)>0):
    ans.append(odd.pop())

while(len(even)>0):
    ans.append(even.popleft())

if n%2==1:ans.reverse()

print(*ans)