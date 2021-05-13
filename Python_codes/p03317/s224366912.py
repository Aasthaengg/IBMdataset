import math
total = 0
N,M = list(map(int,input().split()))
M = M-1
n_l = "".join(input().split())
A = n_l.find("1")
before = A
after = N-A-1
while before > 0:
    before-=M
    total +=1
if before < 0:
    before = abs(before)
    after -= before
while after > 0:
    after-=M
    total +=1
print(total)