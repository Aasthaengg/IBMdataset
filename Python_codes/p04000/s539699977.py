H,W,N = map(int, input().split())

dic = {}
for _ in range(N):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if a+i <= 0 or a+i >= H-1 or b+j <= 0 or b+j >= W-1:
                continue
            if (a+i, b+j) in dic:
                dic[(a+i, b+j)] += 1
            else:
                dic[(a+i, b+j)] = 1
                
ans = [0]*10
for t in dic.values():
    ans[t] += 1
ans[0] = (H-2)*(W-2)-sum(ans)

for i in range(10):
    print(ans[i])