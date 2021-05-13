s = int(input())
a = [s]

for _ in range(1,1000):
    if s % 2 != 0:
        a.append(int(3*s+1))
        s = int(3*s+1)
    else:
        a.append(int(s/2))
        s = int(s/2)

cnt = 0
ans = []

for i,j in zip(a,a[1:]):
    ans.append(i)
    if j in ans:
        ans.append(j)
        print(len(ans))
        break