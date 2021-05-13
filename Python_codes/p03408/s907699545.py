N = int(input())

p_names = []
p_count = []
for n in range(N):
    p_count.append(0)

for n in range(N):
    tmp = input()
    if tmp in p_names:
        index = p_names.index(tmp)
        p_count[index] += 1
    else:
        p_names.append(tmp)
        index = p_names.index(tmp)
        p_count[index] += 1
        
M = int(input())
for m in range(M):
    tmp = input()
    if tmp in p_names:
        index = p_names.index(tmp)
        p_count[index] -= 1
    else:
        continue

if max(p_count)>0:
    print(max(p_count))
else:
    print(0)