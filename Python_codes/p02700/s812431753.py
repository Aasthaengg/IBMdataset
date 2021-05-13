A,B,C,D = map(int,input().split())

taka = 0
aoki = 0

while True:
    if A <= 0:break
    A -= D
    taka += 1

while True:
    if C <= 0:break
    C -= B
    aoki += 1

if taka >= aoki:
    print("Yes")
else:
    print("No")