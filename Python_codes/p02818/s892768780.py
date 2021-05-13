taka,aoki,k = map(int,input().split())
#for i in range(k):
#    if taka >= 1:
#        taka -= 1
#    elif aoki >= 1:
#        aoki -= 1
if k>=taka:
    k -= taka
    taka = 0
    if k>=aoki:
        aoki = 0
    else:
        aoki -= k
else:
    taka -= k
print(taka,aoki)