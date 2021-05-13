N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
cnt = [0]*3

for i in range(N):
    if(P[i] >= B+1):
        cnt[2] += 1
    elif(P[i] <= A):
        cnt[0] += 1
    else:
        cnt[1] += 1
print(min(cnt))