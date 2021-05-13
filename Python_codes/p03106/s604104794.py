a, b, k = [int(i) for i in input().split()]
ans = []
if a > b:
    n = a
elif a < b:
    n = b
else:
    n = a

for x in range(1,n+1):
    if b % x == 0:
        if a % x == 0:
            ans.append(x)

print(ans[-k])