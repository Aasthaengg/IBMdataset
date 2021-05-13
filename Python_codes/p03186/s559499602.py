A,B,C = map(int,input().split())
if A+B >= C-1: ans = B+C
else: ans = (A+B)+1+B
print(ans)