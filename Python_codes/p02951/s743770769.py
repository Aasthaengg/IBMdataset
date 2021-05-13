A, B, C=map(int, input().split())
cap=A-B
C-=min(cap, C)
print(C)