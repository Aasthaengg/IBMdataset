n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = 0
li = []
c = 0
for aa, bb in zip(a, b):
    if bb>aa:
        total += bb-aa
        c += 1
    elif bb<aa:
        li.append(aa-bb)
if c==0:
    print(0)
    exit()
li.sort(reverse=True)
for ans, i in enumerate(li):
    total -= i
    if total<=0:
        print(ans+c+1)
        break
else:
    print(-1)