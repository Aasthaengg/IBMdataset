n = int(input())
b = list(map(int,input().split()))
ans = []
for m in range(n-1,-1,-1):
    for i in range(m,-1,-1):
        if b[i] == i+1:
            ans.append(i+1)
            del b[i]
            break
if b:
    print(-1)
else:
    for i in ans[::-1]:
        print(i)
