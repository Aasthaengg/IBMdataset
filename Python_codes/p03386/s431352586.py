import sys
a,b,k = map(int,input().split())
ans = []
if k > b-a:
    for i in range(a,b+1):
        print(i)
    sys.exit()
    
for i in range(k):
    t1 = a+i
    t2 = b-i
    ans.append(t1)
    ans.append(t2)
A = list(set(ans))
A.sort()

for i in A:
    print(i)