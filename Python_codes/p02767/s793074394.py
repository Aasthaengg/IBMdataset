
N = int(input())
X = list(map(int, input().split()))
ans = 10e9
for i in range(0,max(X)+1):
    tmp = 0
    for j in range(N):
        tmp += (X[j]-i)**2
    if tmp < ans:
        ans = tmp
#    print(tmp)
print(ans)

