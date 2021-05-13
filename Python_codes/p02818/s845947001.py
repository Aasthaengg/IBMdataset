a,b,k = map(int, input().split())
if a <= k:
    a, k = 0, k-a
    b -= k
else:
    a -= k
if b < 0:
    b = 0
print(str(a)+' '+str(b))