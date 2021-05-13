
import heapq

n,k,*td=map(int,open(0).read().split())
td = [[t,d] for t,d in zip(td[::2],td[1::2])]
td = sorted(td,key = lambda x:x[1],reverse=True)

score = [0] * k
taste_sum = 0
extra_taste = []
eat_num = 0
eat_kind = set()

for t,d in td:
    if t in eat_kind:
        if eat_num == k:
            continue
        else:
            heapq.heappush(extra_taste, d)
            taste_sum += d
            eat_num += 1
    else:
        eat_kind.add(t)
        taste_sum += d
        eat_num += 1
        if eat_num > k:
            eat_num -= 1
            taste_sum -= heapq.heappop(extra_taste)
    
    if eat_num == k:
        score[len(eat_kind)-1] = len(eat_kind)**2 + taste_sum
            
    if len(eat_kind) == k:
        break
print(max(score))