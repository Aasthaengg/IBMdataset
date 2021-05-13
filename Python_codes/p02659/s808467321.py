import sys
A, B =map(float,input().split())
A = int(A)
B = int((B+sys.float_info.epsilon*5)*100)
ans = A*B//100
print(ans)
