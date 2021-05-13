A, B, C = map(int,input().split())
for k in range(1,B+1):
    if (A*k)%B == C:
        print("YES")
        exit(0)
print("NO")
