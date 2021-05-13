n, a, b = map(int, input().split())
H = []
for _ in range(n):
    h = int(input())
    H.append(h)

max_t = - (- max(H) // b)

def clear_or_not(a, b, t, H):
    count_t = 0
    for i in range(len(H)):
        need_t = -(-(H[i] - b*t) //(a-b))
        if need_t <= 0:
            need_t = 0
        count_t += need_t
    if count_t <= t:
        return True
    else:
        return False
\
def bisect(low=1, high=max_t):
    while high-low > 1:
        mid = low + (high-low)//2
        if clear_or_not(a,b,mid,H):
            high = mid
        else:
            low = mid
    return high
ans = bisect()

print(ans)
