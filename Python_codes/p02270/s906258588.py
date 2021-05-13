def is_ok(W, limit_num, track_num):
    cu_vol = 0
    cu_tr = 0
    
    for i in range(len(W)):
        if cu_vol + W[i] > limit_num:
            cu_vol = W[i]
            cu_tr += 1
        else:
            cu_vol += W[i]
    if cu_vol:
        cu_tr += 1
    
    return track_num >= cu_tr

n, k = [int(i) for i in input().split()]
W = [int(input()) for _ in range(n)]

top = max(W)
tail = sum(W)
limit_num = 0

while top < tail:
    limit_num = (top + tail) // 2
    if is_ok(W, limit_num, k):
        tail = limit_num
    else:
        top = limit_num + 1

print(tail)


