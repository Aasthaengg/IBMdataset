N = int(input())
# m1,d1=map(int,input().split())
hl = list(map(int, input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
hc = [0 for i in range(N)]
mx = max(hl)
count = 0
for k in range(mx):
    i = 0
    while i < N:
        if hl[i] > hc[i]:
            count += 1
            while i < N and hl[i] > hc[i]:
                hc[i] = hc[i] + 1
                i += 1
        else:
            i += 1
print(count)
