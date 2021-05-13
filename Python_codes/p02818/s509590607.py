a,b,k = map(int,input().split())
takahashi = 0
aoki = 0
if a >= k:
    takahashi = a-k
    aoki = b
else:
    takahashi = 0
    aoki = b-k+a
if aoki < 0:
    aoki = 0
print(takahashi,aoki)