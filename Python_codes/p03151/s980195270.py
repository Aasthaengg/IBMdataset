n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

insufficient = 0
yoyu = []

ans = 0
for i in range(n):
    p = A[i] - B[i]
    if p < 0:#足りない
        insufficient += abs(p)
        ans += 1
    else:
        yoyu.append(p)
yoyu.sort(reverse=True)

if sum(yoyu) < insufficient:
    print(-1)
    exit()

ind = 0    
while insufficient > 0:
    insufficient -= yoyu[ind]
    ind += 1

print(ans+ind)