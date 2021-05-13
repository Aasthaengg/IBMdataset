n, a, b = map(int, input().split())
x = list(map(int, input().split()))
ans = 0

for i in range(len(x)-1):
    here = x[i]
    there = x[i+1]
    if (there - here) * a < b:
        ans += (there - here) * a
    else:
        ans += b

print(ans)


