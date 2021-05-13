#Shiritori
A, B, C = input().split()
if A[-1:] == B[:1]:
    if B[-1:] == C[:1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")