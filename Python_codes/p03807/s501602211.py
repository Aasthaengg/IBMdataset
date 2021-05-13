#template
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
A = inputlist()
co =0
for i in range(N):
    if A[i] % 2 == 1:
        co+=1
if co % 2 == 0:
    print("YES")
else:
    print("NO")