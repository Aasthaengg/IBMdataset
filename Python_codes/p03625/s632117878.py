import collections
n = int(input())
p = list((map(int,input().split())))
x = collections.Counter(p)
y = [i[0] for i in x.items() if i[1]>=2]
z = [i[0] for i in x.items() if i[1]>=4]
y.sort(reverse=True)
y.append(0)
y.append(0)
z.sort(reverse=True)
z.append(0)
ans = y[0]*y[1]
ans1 = z[0]*z[0]
if ans1 > ans:
    ans =ans1
print(ans)
