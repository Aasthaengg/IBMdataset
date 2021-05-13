n = int(input())
a = list(map(int,input().split()))
sum = sum(a)
s = [0]
d = []
q = 0
for i in range(n-1):
    q = s[i]+a[i]
    s.append(q)
    d.append(abs(sum-2*q))

print(min(d))