A,B,C = map(int,input().split())
N = A*B*C
cmin = N
cmin = min(cmin,abs(2*(A//2)*B*C-N))
cmin = min(cmin,abs(2*(B//2)*C*A-N))
cmin = min(cmin,abs(2*(C//2)*A*B-N))
print(cmin)