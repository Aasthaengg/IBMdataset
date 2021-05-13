n,k = map(int, input().split())
w = [int(input()) for i in range(n)]

def track_search(mid):
    count_track = 1
    cnt = 0
    for i in w:
        if i+cnt<=mid:
            cnt+=i
        else:
            count_track += 1
            cnt = i
    return count_track


def weight_search():
    global ans
    right = sum(w)+1
    left = max(w)
    while right>left:
        mid = (right+left)//2
        track = track_search(mid)
        if track>k:
            left = mid+1
        else:
            right = mid
            ans = mid
    return ans

print(weight_search())
