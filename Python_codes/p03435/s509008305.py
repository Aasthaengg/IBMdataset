C=[]
for _ in range(3):
    a = list(map(int, input().split()))
    b = min(a)
    for i in range(3):
        a[i] -= b
    C.append(a)
if C[0] == C[1] == C[2]:
    print("Yes")
else:
    print("No")