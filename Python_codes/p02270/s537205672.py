n, k = map(int, input().split())
w = [int(input()) for i in range(n)]

def f(P):
    i = 0
    for j in range(k):
        s = 0
        while s + w[i] <= P:
            s += w[i]
            i += 1
            if i == n: return n
    return i

left = 0
right = 100000 * 10000

while right - left > 1:
    mid = (left + right) // 2
    v = f(mid)
    if v>=n:right=mid
    else: left = mid
print (right)