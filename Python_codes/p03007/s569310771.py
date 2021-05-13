n = int(input())
a = list(map(int,input().split()))

ans = []
a.sort()
low = a[0]
high = a[-1]
for i in a[1:-1]:
    if i>0:
        ans.append([low,i])
        low = low - i
    else:
        ans.append([high,i])
        high = high - i

ans.append([high,low])
print(high-low)
for x,y in ans:
    print('{0} {1}'.format(x,y))