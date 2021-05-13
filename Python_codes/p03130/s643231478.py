A = list(map(int,(input().split())))
S1 = set(A)
S2 = set(A)
for i in range(2):
    B = list(map(int,input().split()))
    S1 = S1 | set(B)
    S2 = S2 & set(B)
if len(S1) == 4 and len(S2) == 0:
    print("YES")
else:
    print("NO")
