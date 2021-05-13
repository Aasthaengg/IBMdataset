A, B, C = list(map(int,input().rstrip().split()))
print(min(A*B//2,B*C//2,C*A//2))