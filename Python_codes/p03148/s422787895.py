N,K = map(int,input().split())
td = sorted([list(map(int,input().split())) for _ in range(N)],key = lambda x: (-x[1],x[0]))

head = []
no_head = []
is_used = [False]*(N+1)
for t,d in td[:K]:
    if is_used[t]:
        no_head.append(d)
    else:
        head.append(d)
        is_used[t] = True

unused_head = []
for t,d in td[K:]:
    if not is_used[t]:
        unused_head.append(d)
        is_used[t] = True
        
n = min(len(no_head),len(unused_head))
sum_head = sum(head)
sum_no_head = sum(no_head)
sum_unused_head = 0
l_head = len(head)
l_no_head = len(no_head)
ans = sum_head + sum_no_head + l_head ** 2
for i in range(n):
    sum_no_head -= no_head[-1-i]
    sum_unused_head += unused_head[i]
    ans = max(ans,sum_head+sum_no_head+sum_unused_head + (l_head+i+1)**2)
print(ans)