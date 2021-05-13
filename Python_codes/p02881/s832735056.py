n = int(input())
mid = int(n**0.5)
for i in range(mid):
    if n % (mid-i) == 0:
        ans = (mid-i)+(n//(mid-i))
        break
print(ans-2)