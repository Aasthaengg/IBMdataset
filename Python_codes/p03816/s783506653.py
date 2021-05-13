#D
N = int(input())
A = list(map(int,input().split()))

A.sort()

count = 0
old = -1
for a in A:
    if old != a:
        count+=1
        old = a

if count%2 == 1:
    print(count)
else:
    print(count-1)

