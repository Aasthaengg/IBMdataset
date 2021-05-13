n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
ab = sorted(ab,key=lambda x: x[1])
ans = 'No'
t = 0

for i in ab:
    t += i[0]
    if i[1] < t:
        break
else:
    ans = 'Yes'

print(ans)