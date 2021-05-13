N = int(input())
S = list(input())
S.append("a")
n = list(map(str,range(0,10)))
ans = 0
for i in n:
    for j in n:
        for k in n:
            num = i+j+k
            now = 0

            for l in range(N+1):
                if now == 3:
                    ans += 1
                    break
                if num[now] == S[l]:
                    now += 1
print(ans)