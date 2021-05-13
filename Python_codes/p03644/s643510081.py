n = int(input())
a = [0]*n
j = 0
for i in range(1, n+1):
    while True:
        if i%2!=0:
            break
        i=i//2
        if i==0:
            break
        else:
            a[j]+=1
    j+=1
maxv = max(a)
maxi = a.index(maxv)
print(maxi+1)
