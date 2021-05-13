n, k = list(map(int, input().split()))
v = list(map(int, input().split()))
l = 0
r = 0
a = 0
m = min(n, k)+1
have = []
total = 0
ans = 0
for r in range(m):
    for l in range(m-r):
        have = []
        have.append(v[:r])
        if l != 0:
            have.append(v[-l:])
        else:
            have.append([])
        a = k-l-r
        data = have[0]+have[1]
        data.sort()
        for i in range(len(data)):
            if i < a and data[i] < 0:
                data[i] = 0
        total = sum(data)
        if total > ans:
            ans = total
print(ans)
