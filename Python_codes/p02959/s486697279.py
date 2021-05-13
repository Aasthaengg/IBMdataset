# https://atcoder.jp/contests/abc135/tasks/abc135_c
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
tmp = 0
for i in range(n):
    #print(i,tmp)
    #print(a)
    #print(b)
    if tmp > 0:
        if a[i] <= tmp:
            ans += a[i]
            a[i] = 0
            tmp = b[i]
        else:
            ans += tmp
            a[i] -= tmp
            tmp = 0
    if a[i] > 0:
        if a[i] <= b[i]:
            ans += a[i]
            tmp = b[i] - a[i]
            a[i] = 0
            b[i] = tmp
        else:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
            tmp = 0
tmp = min(tmp,a[-1])
#print(a)
#print(b)
#print(tmp)
print(ans+tmp)