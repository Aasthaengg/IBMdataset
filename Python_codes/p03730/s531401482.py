import sys
A,B,C = map(int,input().split())

if A < 0 or A > 100 or B < 0 or B > 100:
    sys.exit()
if not ( C >= 0 or C < B ):
    sys.exit()

tmp = 0
result = "NO"
for I in range(B):
    tmp = A * I % B
    if tmp % B == C:
        result = "YES"

print(result)