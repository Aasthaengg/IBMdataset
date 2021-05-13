n = int(input())
a = list(map(int,input().split()))
res = 0
i = 0
if n%2:
    a.append(a[n-1]+1)
#print(a)

while i < n-1:
    if a[i] == a[i+1]:
        res += 1
        i+=1
    i+=1
print(res)