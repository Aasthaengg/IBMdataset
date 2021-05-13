import sys
A,B = map(int,input().split())
if not ( 10000 <= A <= B <= 99999 ):
    sys.exit()

count = 0
for I in range(A,B+1):
    if str(I) == str(I)[::-1]:
        count += 1
print(count)