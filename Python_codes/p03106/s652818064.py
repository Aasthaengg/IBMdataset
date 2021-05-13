A,B,K = map(int,input().split())

count = 0
import math
R = []
for i in range(1,int(math.sqrt(A))+1+1):
    if A%i == 0:
        R.append(i)
        if not i == A//i:
            R.append(A//i)
R.sort(reverse=True)
for r in R:
    if B%r==0:
        count+=1
        if count == K:
            print(r)



