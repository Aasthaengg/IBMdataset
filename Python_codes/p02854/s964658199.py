n = int(input())
a = list(map(int,input().split()))
s = sum(a)
d = s // 2
t = 0
i = -1
while(t <= d):
    i += 1
    t += a[i]
t2 = t - a[i]
# print(t,t2,s)
# print(t-(s-t),(s-t2)-t2)
print(min(t - (s - t),(s - t2) - t2))