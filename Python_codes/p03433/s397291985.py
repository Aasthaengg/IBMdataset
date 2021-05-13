N=int(input())
A=int(input())

while N>=500:
    N-=500

if A>=N:
    print("Yes")
else:
    print("No")
