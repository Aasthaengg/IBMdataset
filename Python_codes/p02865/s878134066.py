N = int(input())
cnt=0
for i in range(1, N):
    k = N-i
    if i<k:
        cnt+=1
print(cnt)