A, B = map(int, input().split())
s = B - A
t = 0
for i in range(1,s + 1):
    t += i
ans = t - B
print(ans)
