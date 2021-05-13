import copy
n = int(input())
vote_ls = [[0,0] for _ in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    vote_ls[i] = [a,b]

def check(previous,now):
    ok = True
    for j in [0,1]:
        if previous[j] > now[j]:
            ok = False
    return ok

previous = vote_ls[0]
for i in range(1,n):
    now = copy.copy(vote_ls[i])
    if check(previous,now):
        previous = now
        continue

    time_a = -(-previous[0]//now[0])
    time = float('inf')
    if now[1] * time_a >= previous[1]:
        time = min(time,time_a)
    time_b = -(-previous[1]//now[1])
    if now[0] * time_b >= previous[0]:
        time = min(time,time_b)
    now[0]*=time
    now[1]*=time
    previous = now

print(sum(previous))