N = int(input())
dlst = [int(input()) for i in range(N)]
list.sort(dlst)
answer = 1
for i in range(1,N):
    if dlst[i] != dlst[i - 1]:
        answer += 1
print(answer)
