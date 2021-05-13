N,P = map(int,input().split())
A = list(map(int,input().split()))

su = 2 ** N
guusu = True
for a in A:
    if a % 2 == 1:
        guusu = False
        break
if P == 0:
    print(su if guusu else su//2)
else:
    print(0 if guusu else su//2)