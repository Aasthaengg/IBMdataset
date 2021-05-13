N = int(input())
A = list(map(int,input().split()))
c = [0] * 9
for i in A:
    if i < 3200:
        c[i//400]+=1
    else:
        c[8]+=1
cnt = 0
for i in range(8):
    if c[i] != 0:
        cnt += 1
mini = max(1,cnt)
maxi = cnt+c[8]
print(mini,maxi)
