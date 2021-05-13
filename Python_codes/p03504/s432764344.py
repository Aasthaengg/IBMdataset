from operator import itemgetter
N,C = [int(x) for x in input().split()]
# list(time,action,channel) action = start:1, stop:0
actions = []
for _ in range(N):
    s,t,c = [int(x) for x in input().split()]
    actions.append((s-0.5, 1, c))
    actions.append((t, 0, c))
actions.sort(key=itemgetter(0))

cnt_now_rec = 0
# list to know the start time of rec. if channel not in rec, takes -1.
channel_now_rec = [-1] * (C+1)
ans = 0
for time,action,channel in actions:
    if(action == 1):
        if(channel_now_rec[channel]==-1):
            cnt_now_rec += 1
        channel_now_rec[channel] = time
    elif(action == 0):
        if(time == channel_now_rec[channel]+0.5):
            pass
        else:
            cnt_now_rec -= 1
            channel_now_rec[channel] = -1
    ans = max(ans,cnt_now_rec)
print(ans)
