x,a,b = map(int,input().split())
A= 1
syoumikigen = A + a
B = A + b
safe = syoumikigen + x
out = safe + 1
if B <= syoumikigen:
    print("delicious")
elif syoumikigen < B <= safe:
    print("safe")
else:
    print("dangerous")  


