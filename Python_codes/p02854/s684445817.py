n = int(input())
a = list(map(int, input().split()))
SUM = sum(a) 
ans = []
l = [[0, SUM]]
for i in range(n):
    l.append([l[i][0] + a[i], SUM - (l[i][0] + a[i])])
for i in l:
    ans.append(abs(i[0] - i[1]))
print(min(ans))