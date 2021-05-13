r,c = map(int,input().split())
rc=[]
total=[]
for _ in range(r): rc.append(list(map(int,input().split())))
for i in range(r): rc[i].append(sum(rc[i]))
for i in zip(*rc): total.append(sum(i))
rc.append(total)
for col in rc: print(*col)