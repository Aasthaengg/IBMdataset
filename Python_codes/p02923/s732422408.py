n = int(input())
h = list(map(int,input().split()))

cnt = 0
lst = [0]
for i in range(n-1):
    if h[i] >= h[i+1]:
        cnt += 1
        lst.append(cnt)
    else:
        cnt = 0

print(max(lst))