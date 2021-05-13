
n = int(input())

li = list(map(int,input().split()))

l = []

t = li[0]
for i in range(1,len(li)):
    if t >= li[i]:
        l.append(t - li[i])
    else:
        l.append(0)
        t =li[i]

print(sum(l))
