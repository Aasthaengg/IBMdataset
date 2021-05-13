n, k = map(int,input().split())
x = (n-2)*(n-1)//2

if k > x:
    print(-1)
    exit()

ans = []
for i in range(2, n+1):
    ans.append([1, i])
i = 2
j = 3
while k < x:
    ans.append([i, j])
    if j < n:
        j += 1
    else :
        i += 1
        j = i+1
    x -= 1 

print(len(ans))
for i in range(len(ans)):
    b = [str(i) for i in ans[i]]
    print(' '.join(b))