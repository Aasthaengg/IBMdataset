def check(P,w,n):
    i = 0
    for j in range(k):
        s = 0
        while s + w[i] <= P:
            s += w[i]
            i += 1
            if i == n:
                return n
    return i

s = input().split(" ")
n = int(s[0])
k = int(s[1])
w = []
for i in range(n):
    a = int(input())
    w.append(a)

left = 0
right = 100000 * 10000
while right - left > 1:
    mid = int((right + left) / 2)
    v = check(mid,w,n)
    if v >= n:
        right = mid
    else:
        left = mid
print(right)