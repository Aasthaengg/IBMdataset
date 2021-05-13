N = int(input())
A = [list(input().split()) for _ in range(N)]
x = input().strip()
for i in range(N):
    if A[i][0]==x:
        ind = i
        break
cnt = 0
for i in range(ind+1,N):
    cnt += int(A[i][1])
print(cnt)