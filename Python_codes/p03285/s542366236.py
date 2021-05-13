N = int(input())

if N%2==1:
    N = N-7
if N%4==2:
    N = N-14
if (N%4==0)and(N>=0):
    print("Yes")
else:
    print("No")
