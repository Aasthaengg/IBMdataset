n = int(input())
l = []

def each_sum(x):
    y = str(x)
    ans = 0
    for i in range(len(y)):
        ans += int(y[i])
    return ans

for a in range(1, n):
    b = n - a
    l.append(each_sum(a) + each_sum(b))

print(min(l))