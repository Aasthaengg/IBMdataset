x, y, a, b, c = map(int,input().split())
p_p = list(map(int,input().split()))
q_q = list(map(int,input().split()))
r_r = list(map(int,input().split()))
p_p.sort(reverse=True)
q_q.sort(reverse=True)
r_r.sort(reverse=True)

oisisa = sum(p_p[:x])+sum(q_q[:y])
apple = p_p[:x] + q_q[:y]
apple.sort()
seen = 0
for i in range(min(x+y,c)):
    if r_r[i] > apple[seen]:
        oisisa = oisisa + r_r[i] - apple[seen]
        seen += 1
    else:
        break


print(oisisa)