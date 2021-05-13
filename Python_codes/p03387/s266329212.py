A,B,C = sorted(int(X) for X in input().split())
Count = 0
if A!=C and B!=C:
    Count += C-B
    A += C-B
if A!=C:
    Count += (C-A)//2 + 2*((C-A)%2!=0)
print(Count)