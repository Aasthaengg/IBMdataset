a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a2 = (a+9)//10 * 10
b2 = (b+9)//10 * 10
c2 = (c+9)//10 * 10
d2 = (d+9)//10 * 10
e2 = (e+9)//10 * 10

sum = a2+b2+c2+d2+e2
ans = 1e18
ans = min(ans, sum-a2+a)
ans = min(ans, sum-b2+b)
ans = min(ans, sum-c2+c)
ans = min(ans, sum-d2+d)
ans = min(ans, sum-e2+e)

print(ans)