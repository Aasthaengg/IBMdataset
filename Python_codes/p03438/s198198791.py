n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ca = 0
cb = 0
for aa, bb in zip(a, b):
    if aa < bb:
        cb += (bb - aa)//2
    if bb < aa:
        ca += aa - bb
# print(ca, cb)
if cb >= ca:
    print('Yes')
else:
    print('No')
