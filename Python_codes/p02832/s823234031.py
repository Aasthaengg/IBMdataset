N = int(input())
a_s = list(map(int, input().split()))
cnt = 1
answer = 0
for i, a in enumerate(a_s):
    if cnt == a:
        cnt += 1
    else:
        answer += 1
if answer == N:
    print(-1)
else:
    print(answer)