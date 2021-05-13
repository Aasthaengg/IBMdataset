A, B, C = (int(i) for i in input().split())

first = min(B, C)

B = B - first
C = C - first

if(B == 0):
    if(A >= C-1):
        second = C
    else:  # A>=C
        second = min(A, C)+1
else:  # C==0
    second = B

print(int(first * 2 + second))
