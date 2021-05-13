A,B = (int(i) for i in input().split())
ans = max(A+B,A-B,A*B)
print(ans)