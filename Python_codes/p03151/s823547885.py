n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
    exit()
dif = []
for i in range(n):
    dif.append(a[i]-b[i])
dif.sort()
dif += [0]
ans = 0
i = n
for x in dif:
    if x<0:
        ans += 1
        while x<0:
            if dif[i]<-x:
                x += dif[i]
                i -= 1
                ans += 1
            else:
                dif[i] += x
                x = 0
    else:break
print(ans)
