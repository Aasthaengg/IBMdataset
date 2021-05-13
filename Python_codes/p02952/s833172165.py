n=int(input())
a = [str(i) for i in range(1,n+1)]
res = 0
for i in a:
    if len(i)%2==1:
        res += 1
print(res)