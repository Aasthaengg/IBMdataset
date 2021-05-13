N = int(input())
H = list(map(int,input().split()))

maxim = 0
count = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        count += 1
    else:
        count = 0
    if count > maxim:
        maxim = count
print(maxim)