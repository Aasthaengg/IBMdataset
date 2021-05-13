n = int(input())
a = 0
b = 0
ans = 1000000000
for i in range(1, n):
    a = n - i
    b = n - a
    a = list(map(int,str(a)))
    b = list(map(int,str(b)))
    if sum(a) + sum(b) <= ans:
        ans = sum(a) + sum(b)
print(ans)
