N,L = map(int,input().split())

diffabs = 99999
taste = 0

for i in range(N):
    taste += L+i
    if abs(L+i)<diffabs:
        diffabs = abs(L+i)
        diff = L+i
print(taste-diff)