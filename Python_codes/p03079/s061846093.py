A, B, C = map(int, input().split())

result = False
if A == B:
    if B == C:
        result = True

if result:
    print("Yes")
else:
    print("No")
