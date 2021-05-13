#23 A - A+...+B Problem
N,A,B = map(int,input().split())

if A<=B:
    ans = (B*(N-2)) - (A*(N-2)) + 1
else:
    ans = 0
if ans<0:
    ans = 0
print(int(ans))