n = int(input())
l = list(map(int, input().split()))
s = sum(l)
evens = 0
for i in range(1, n, 2):
    evens += 2*l[i]
x1 = s - evens
ans = [x1]
for i in range(n-1):
    temp = l[i] - ans[-1]//2
    ans.append(2*temp)
print(*ans)

