N,L = map(int,input().split())
count = L
taste = []
for i in range(N):
    taste.append(count)
    count += 1
if 0 in taste:
    taste.remove(0)
elif  N + L <= 0:
    taste.pop(-1)
else:
    taste.pop(0)
print(sum(taste))