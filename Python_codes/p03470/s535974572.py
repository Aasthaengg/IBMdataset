n = int(input())
d = []
cnt = 1
for i in range(n):
    d.append(int(input()))
d.sort(reverse=True)
_ = d[0]
for j in range(n-1):
    if _ > d[j+1]:
        cnt += 1
        _ = d[j+1]
print(cnt)
