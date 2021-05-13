n = int(input())
h = list(map(int,input().split()))
cnt = 0
lis = [0]
for i in range(n-1):
    if h[i] >= h[i+1]:
        cnt += 1
    else:
        lis.append(cnt)
        cnt = 0
lis.append(cnt)
print(max(lis))