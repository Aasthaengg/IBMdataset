N, K = map(int,input().split())
w = [int(input()) for i in range(N)]

def check(p):
    track = 0
    tmp_w = 0
    for i in range(N):
        if w[i] > p:
            return False
        else:
            if (tmp_w + w[i]) > p:
                track += 1
                tmp_w = w[i]
            else:
                tmp_w += w[i]
    if track + 1 > K:
        return False
    else:
        return True

left = 0
right = 2000000000
while((left + 1) < right):
    mid = (left + right) // 2
    track = check(mid)
    if check(mid):
        right = mid
    else:
        left = mid 
        
print(right)
