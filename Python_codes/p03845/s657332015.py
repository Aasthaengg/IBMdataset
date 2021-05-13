N = int(input())
T = list(map(int, input().split()))
sum_ = sum(T)
M = int(input())
ans = list()
for i in range(M) :
    P, X = map(int,input().split())
    gap = T[P-1] - X
    ans.append(sum_ - gap)

for i in range(len(ans)):
    print(ans[i])
