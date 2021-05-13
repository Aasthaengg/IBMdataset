n = int(input())
a = list(map(int,input().split()))
t = [0]
for i in range(n):
    t.append(t[i] + a[i])
t.pop(0)
p = t[-1] // 2
if p in t:
    print(0)
else:
    for i in range(n):
        if p < t[i]:
            print(min(abs(sum(a[0:i+1]) - sum(a[i+1:n])),abs(sum(a[0:i]) - sum(a[i:n]))))
            break