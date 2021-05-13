n,a,b=map(int,input().split())
lists=[]
for i in range(n):
    s=int(input())
    lists.append(s)

start=0
end=10**9
import math

for _ in range(30):
    sub=0
    judge=(start+end)/2
    for some in lists:
        sub+=max(0,math.ceil((some-b*math.floor(judge))/(a-b)))

    if sub<judge:
        start=start
        end=judge
    elif sub>=judge:
        start=judge
        end=end
print(math.floor(start)+1)