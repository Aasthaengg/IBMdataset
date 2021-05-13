n = int(input())
a = [int(v) for v in input().split()]
a.sort()
a.append(-1)
d = 1
for i in range(0, n):
    if(a[i] == a[i + 1]):
        d = 0
        print("NO")
        break
if(d == 1):
    print("YES")
