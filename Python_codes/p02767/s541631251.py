n=int(input())
x = list(map(int,input().split()))
y =[]
b = sum(x)
for i in range(n):
        y.append((x[i])**2)
a = sum(y)

p = round(b/(n))
ans = (n)*p**2-2*p*b+a
print(ans)