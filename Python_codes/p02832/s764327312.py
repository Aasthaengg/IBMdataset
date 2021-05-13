N = int(input())
a = list(map(int, input().split()))
count = 1
unbreak = 0

for i in range(N):
    if a[i] == count:
        count+=1
        unbreak +=1

if unbreak == 0:
    print(-1)
else:
    print(N-unbreak)
