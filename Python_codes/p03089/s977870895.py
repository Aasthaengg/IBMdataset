n = int(input())
b = list(map(int, input().split()))
ans = []
while b:
    for i, j in enumerate(reversed(b)):
        if j==len(b)-i:
            ans.append(j)
            del b[len(b)-i-1]
            break
    else:
        print(-1)
        break
else:
    for i in reversed(ans):
        print(i)