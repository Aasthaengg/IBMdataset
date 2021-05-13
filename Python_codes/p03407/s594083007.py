#91

A, B, C = map(int, input().rstrip().split())

if C-(A+B) <= 0:
    print("Yes")
else:
    print("No")