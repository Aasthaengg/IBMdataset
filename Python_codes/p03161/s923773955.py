n,k = map(int,input().split())
l = list(map(int,input().split()))
a = [0]*n
a[1] = abs(l[0]-l[1])
i = 2
while(i < len(a)):
    e = i-k
    ma = 10**10
    j = i-1
    while(j > -1 and j >= e):
        r = a[j]+abs(l[i]-l[j])
        ma = min(ma,r)
        j = j-1

    a[i] = ma
    i = i+1

#print(a)
print(a[-1])