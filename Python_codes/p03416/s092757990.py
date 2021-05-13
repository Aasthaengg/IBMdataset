A,B = (int(X) for X in input().split())
Count = 0
for T in range(A,B+1):
    StrT = str(T)
    if StrT[0:2]==StrT[3:5][::-1]:
        Count += 1
print(Count)