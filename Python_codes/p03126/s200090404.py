n,m = map(int,input().split())
ans = [0]*m
for _ in range(n):
    T = list(map(int,input().split()))
    for i in range(1,len(T)):
        ans[T[i]-1] += 1


ans_s = 0
for a in ans:
    if a == n:
        ans_s += 1

print(ans_s)