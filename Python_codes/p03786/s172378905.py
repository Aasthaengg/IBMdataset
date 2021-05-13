n = int(input())
a = sorted(map(int, input().split()))
cs = [0]
for i in range(n):
    cs.append(cs[i]+a[i])

# print(cs)
ans = 1
for i in range(n-1)[::-1]:
    if 2*cs[i+1] >= a[i+1]:
        ans += 1
    else:
        break
        # print(i)

print(ans)