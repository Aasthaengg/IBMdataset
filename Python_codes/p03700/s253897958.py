n, a, b = map( int, input().split() )
h = [ int(input()) for _ in range(n) ]

def judge(k):
    _sum = 0
    for hh in h:
        t = hh-k*b
        if t > 0:
            _sum += (t+a-b-1) // (a-b)
            if _sum > k:
                return False;
    return True


high, low = int(1e9+9), 0

while low < high:
    mid = int((high + low) / 2)
    if judge(mid):
        high = mid;
    else:
        low = mid+1;

print(low)
