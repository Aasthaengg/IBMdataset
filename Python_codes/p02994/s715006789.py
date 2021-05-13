n, l = map(int, input().split())
s = sum(range(l, n+l))
ans = -1
ans_dif = 10**9
for i in range(l, n+l):
    if ans_dif > abs(s - (s - i)) :
        ans_dif = abs(s - (s - i))
        ans = s - i
print(ans)
