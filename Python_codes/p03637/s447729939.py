import math

n = int(input())
s = list(map(int,input().split()))

mul2 = 0
mul4 = 0
for i in s:
    if i%4 == 0:
        mul4 += 1
    elif i%2 == 0:
        mul2 += 1

if mul4 >= math.floor(n/2):
    print("Yes")
elif mul2 == n:
    print("Yes")
elif n-mul2-mul4-1+mul2%2 <= mul4:
    print("Yes")
else:
    print("No")