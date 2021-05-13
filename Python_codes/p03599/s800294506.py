from collections import deque
a,b,c,d,e,f = map(int,input().split())

def judgement(x,y):
    flag = True
    if 100*y > e*x:
        flag = False
    if x+y > f:
        flag = False
    return flag


q = deque([(100*a, 0)])
used = set()
used.add((100*a, 0))
if 100*b <= f:
    q.append((100*b, 0))
    used.add((100*b, 0))
ans = (100*a,0)
per = 0
while q:
    tar = q.popleft()
    step = [(tar[0]+100*a, tar[1]), (tar[0]+100*b, tar[1]),
            (tar[0], tar[1]+c), (tar[0], tar[1]+d)]
    for i in step:
        if i not in used:
            used.add(i)
            if judgement(i[0], i[1]):
                q.append(i)
                if per*i[0] < i[1]:
                    per = i[1]/i[0]
                    ans = i
print(ans[0]+ans[1], ans[1])





