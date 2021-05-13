A,B,C = [int(i) for i in input().split()]
D = max(A,B)
for i in range(1,D+1):
    if A * i % B == C:
        print("YES")
        break
    if A * i % B != C and i == D:
        print("NO")
