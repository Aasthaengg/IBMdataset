n = int(input())

a = []

for i in range(1,n+1):
    if (i % 5 == 0) and (i % 3 == 0):
        continue
    elif i % 5==0:
        continue
    elif i % 3 ==0:
        continue
    else:
        a.append(i)
    
ans = sum(a)

print(ans)