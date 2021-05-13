x,y,a,b,c = list(map(int, input().split()))

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p_rev = sorted(p, reverse=True)
q_rev = sorted(q, reverse=True)
pq_rev = sorted(p_rev[:x] + q_rev[:y] , reverse=True)

total = sum(sorted(pq_rev + r, reverse=True)[:x+y])
print(total)