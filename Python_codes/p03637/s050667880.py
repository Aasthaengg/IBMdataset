N=int(input())
A = list(map(int, input().split()))
b4 = 0
b2 = 0
other = 0
for a in A:
    if a%4==0:
        b4 += 1
    elif a%2 == 0:
        b2 += 1
    else:
        other += 1

if N % 2 == 1:
    if b4 < other - 1:
        print("No")
    else:
        print("Yes")
else:
    if b4 < other:
        print("No")
    else:
        print("Yes")
