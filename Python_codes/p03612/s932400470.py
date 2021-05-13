N = int(input())
P = list(map(int, input().split()))

def swap(i, j):
    return j, i

now = P[0]
count = 0
for i in range(N-1):
    after = P[i+1]
    if now == i+1:
        now, after = swap(now, after)
        count += 1    
    now = after

if now == N:
    count += 1
    
print(count)