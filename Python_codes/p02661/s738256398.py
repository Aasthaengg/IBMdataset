n = int(input())
a = [0]*n
b = [0]*n
for i in range(n): a[i],b[i] = map(int,input().split())
a.sort()
b.sort()
if n%2 == 1:
    m = n//2
    ans = b[m] - a[m] + 1
else:
    ml = n//2-1
    mr = n//2
    ma = (a[ml] + a[mr])/2 
    mb = (b[ml] + b[mr])/2
    ans = int((mb - ma)*2 + 1)
print(ans) 