N = int(input())

works = []
for work in range(N):
    a, b = [int(i) for i in input().split()]
    works.append((a, b))
    
works.sort(key=lambda x: x[1])

time_cnt = 0
flag = True
for work in works:
    t = work[0]
    l = work[1]
    time_cnt += t
    if time_cnt > l:
        flag = False
        break
        
if flag:
    print('Yes')
else :
    print('No')