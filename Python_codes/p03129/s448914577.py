n,k = map(int,input().split())
x = [i for i in range(n+2) if i % 2 == 1]
for i in range(len(x)):
    if x[i] >=100:
        x.pop(i)

if int(len(x)) >= k:
    print("YES")
else:
    print("NO")