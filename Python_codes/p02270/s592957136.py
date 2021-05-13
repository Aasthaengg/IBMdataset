n,k = map(int,input().split())
wi = []
for _ in range(n):
    wi.append(int(input()))

def isPossibleCarry(k, wi, P):
    track_num = 1
    track_weight = 0
    
    for w in wi:
        if(w > P):
            return False
        
        if(track_weight + w < P):
            track_weight = track_weight + w
        elif(track_weight + w == P):
            track_num += 1
            track_weight = 0
        else:
            track_num += 1
            track_weight = w
            if(track_num > k):
                return False
            
    return track_num <= k or (track_num == k+1 and track_weight==0)

left_P = 1
right_P = sum(wi)
while left_P < right_P:
    mid = int((left_P + right_P) /2)
    if(isPossibleCarry(k, wi, mid)):
        right_P = mid
    else:
        left_P = mid + 1
if(isPossibleCarry(k, wi, mid)):
    print(mid)
else:
    print(left_P)

