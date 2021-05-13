ans = 'No'
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        if max(i,n/i) < 10:
            ans = 'Yes'
print(ans)