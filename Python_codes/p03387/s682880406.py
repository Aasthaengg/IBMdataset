A = list(map(int, input().split()))
A.sort()
DifA = A[2] - A[1]
DifB = A[2] - A[0]
#print(DifA,DifB)
if DifA % 2 == 0 and DifB % 2 == 0:
    ans = ( DifA + DifB ) // 2
elif DifA % 2 == 1 and DifB % 2 == 1:
    ans = ( DifA + DifB ) // 2
else:
    ans = ( DifA + DifB + 3 ) // 2
print(ans)