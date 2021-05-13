a,b = map(int, input().split())

res = 0
for i in range(a,b+1):
    ii = str(i)
    iir = ii[::-1]
    if iir == ii :
        res +=1
        
print(res)