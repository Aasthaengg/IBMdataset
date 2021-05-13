A,B = map(int,input().split())
ls = []
a = 0
for i in range(1,1000):
    a += i
    ls.append(a)
sa = B-A
ans = ls[sa-1] - B
print(ans)