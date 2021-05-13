n = int(input())
a = list(map(int , input().split()))
pos = sorted([i for i in a if i >= 0], reverse=True)
neg = sorted([i for i in a if i < 0], reverse=True)

ans = []
if len(neg) == 0 and len(pos) == 2:
    print(pos[0] - pos[1])
    print(pos[0], pos[1])
    exit()
elif len(pos) == 0:
    tmp = neg[0]
    for i in range(1,len(neg)):
        ans.append([tmp, neg[i]])
        tmp -= neg[i]
    print(tmp)
    [print(*i) for i in ans]
    exit()
elif len(neg) == 0:
    neg.append(pos.pop())

tmp = neg.pop()
while len(pos) > 1:
    a = pos.pop()
    ans.append([tmp, a])
    tmp -= a
neg.append(tmp)

tmp = pos[0]
for i in neg:
    ans.append([tmp, i])
    tmp -= i

print(tmp)
[print(*i) for i in ans]
