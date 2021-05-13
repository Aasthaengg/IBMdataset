N = int(input())
ls = list(map(int, input().split()))

ans = [float('inf')] * N
ans[0] =0
ans[1] = abs(ls[1]-ls[0])
for i in range(2, N):
    ans[i] = min(ans[i-1]+ abs(ls[i]-ls[i-1]), ans[i-2]+ abs(ls[i]-ls[i-2]))

print(ans[-1])