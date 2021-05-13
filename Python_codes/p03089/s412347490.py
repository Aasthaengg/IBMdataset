N = int(input())
B = list(map(int,input().split()))

ans = []
while len(ans) < N:
    j = -1
    for i,b in enumerate(B):
        if b==i+1:
            j = i
    if j==-1:
        print(-1)
        exit()
    ans.append(j+1)
    del B[j]
print(*ans[::-1], sep='\n')