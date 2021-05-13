A, B = map(int,input().split())
r = max(A-B, A+B, A*B)
print(int(r))