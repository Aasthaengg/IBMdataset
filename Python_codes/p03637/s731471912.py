from collections import deque

def f(x):
    return num.count(x)

n = int(input())
a = list(map(int, input().split()))
num = deque([])
for i in a:
    if i%4==0:
        num.append(4)
    elif i%2==0:
        num.append(2)
    else:
        num.append(0)

if len(a)%2==1:
    if f(4)>=len(a)//2 or f(2)>=2*(n//2-f(4))+1:
        print('Yes')
        exit(0)
if len(a)%2==0:
    if f(2)>=2*(n//2-f(4)):
        print('Yes')
        exit(0)
print('No')
