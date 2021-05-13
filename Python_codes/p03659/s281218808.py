n = int(input())
a = [int(x) for x in input().split()]
 
x = 0
ans = []
suma = sum(a)
 
for i in a[:-1]:
    x += i
    ans.append(abs(suma - x * 2))
else:
    print(min(ans))