A, B, C = map(str, input().split())

if A[-1] == B[0]:
    if B[-1] == C[0]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")