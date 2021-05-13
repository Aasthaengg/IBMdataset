N, M,X,Y=[int(i) for i in input().split()]
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
mx = max(x)
my = min(y)
ok = False
for i in range(X+1, Y+1):
   if mx<i and i<=my:
     ok =True

if ok:
    print("No War")
else:
    print("War")