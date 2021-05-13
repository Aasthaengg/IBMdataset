import sys
A,B = map(int,input().split())
if not ( 3 <= A <= 20 and 3 <= B <= 20 ): sys.exit()

sum = 0
for I in range(2):
    sum += A if A > B else B
    if A > B:
         A -= 1
    else:
         B -= 1
print(sum)