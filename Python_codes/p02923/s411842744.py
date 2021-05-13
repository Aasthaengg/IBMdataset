N = int(input())
H = list(map(int,input().split()))
step = 0
answer = 0
for i in range(N-1):
    if H[i]>=H[i+1]:
        step += 1
    if H[i]<H[i+1] or i==N-2:
        answer = max(answer,step)
        step = 0
print(answer)