N = int(input())
b = list(map(int, input().split()))
ans = []

for _ in range(N):
    for i in range(len(b)-1, -1, -1):
        if b[i]==i+1:
            ans.append(b[i])
            b = b[:i]+b[i+1:]
            break
    else:
        print(-1)
        exit()

ans.reverse()

for ans_i in ans:
    print(ans_i)