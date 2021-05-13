n = int(input())
t,a = map(int, input().split())
dat = list(map(int, input().split()))
resind = -1
resval = 9999999999999999999999999
for i in range(n):
    x = t - dat[i] * 0.006
    diff = abs(x-a)
    if diff < resval:
        resval = diff
        resind = i
print(resind+1)
