n=int(input())

print(n*(n-1)//2-n//2)
if n%2:
    wa=n
else:
    wa=n+1
for i in range(1,n+1):
    for ii in range(1,i):
        if i+ii!=wa:
            print(ii,i)