n,k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

def sim(start,mx): # simulate mx step from start, returns max_score
    if mx==0:
        return 0
    now_p=0
    nxt=p[start]-1
    cnt=0
    p_lis=[]

    while True:
        nxt=p[nxt]-1
        now_p+=c[nxt]
        p_lis.append(now_p)
        cnt+=1
        if cnt==mx:
            break

    return max(p_lis)

visited_p=set() # already checked flag
cycle_score=[] # cycle loop score
cycle_points=[]
now_cycle=0

for i in range(n):
    if i in visited_p:
        continue
    visited_p.add(i)
    now_p=0
    nxt=p[i]-1
    visited=set()
    while True:
        nxt=p[nxt]-1
        visited_p.add(nxt)
        if nxt in visited:
            break
        visited.add(nxt)
        now_p+=c[nxt]
    cycle_score.append(now_p)
    cycle_points.append(list(visited))

ans=-float('inf')

for c_num in range(len(cycle_score)):
#    print(c_num,cycle_score[c_num],cycle_points[c_num])
    cycle_len=len(cycle_points[c_num])
    for start in cycle_points[c_num]:

        if cycle_score[c_num]<0: # no loop, just check min(loop_len,k)
            score = sim(start,min(cycle_len,k))
            ans=max(ans,score)

        else: # loop as many as possible
            loop_num = max(0,(k // cycle_len) - 1)
            nokori=k-loop_num*cycle_len
            score = sim(start,nokori) + loop_num*cycle_score[c_num]
            ans=max(ans,score)

print(ans)

