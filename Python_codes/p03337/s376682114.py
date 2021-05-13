A, B = [int(ab) for ab in input().split()]
C = A+B
D = A-B
E = A*B
ans = max(C, D, E)
print(ans)