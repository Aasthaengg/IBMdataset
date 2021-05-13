n,m = map(int, input().split())

cnt = [0]*m

for i in range(n):
    survey = list(map(int, input().split()))
    k = survey[0]
    for j in range(1,k+1):
        favorite = survey[j]
        cnt[favorite - 1] += 1

print(cnt.count(n))