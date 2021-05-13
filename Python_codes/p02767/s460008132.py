def dist(x, p):
    return (x - p)**2


n = int(input())
x = [int(i) for i in input().split()]
index = len(x) // 2
new_x = sorted(x)
p1 = - (- sum(x) // len(x))
p2 = sum(x) // len(x)
ans = [0, 0]
for i in new_x:
    ans[0] += dist(i, p1)
    ans[1] += dist(i, p2)
print(min(ans))