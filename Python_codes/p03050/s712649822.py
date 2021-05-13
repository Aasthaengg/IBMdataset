n = int(input())
d = []
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        d.append(i)
ans = 0
for i in d:
    if (n//i-1) > i:
        ans += n//i -1
print(ans)