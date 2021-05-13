N=int(input())
h=list(map(int,input().split()))
answer=0
for n in range(N-1):
    if h[n]>h[n+1]:
        answer+=h[n]-h[n+1]
answer+=h[-1]
print(answer)
