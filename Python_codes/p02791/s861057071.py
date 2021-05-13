number = int(input())
score = list(map(int,input().split()))
minn = score[0]
answer = 0
for i in range(number):
    if minn >= score[i]:
        answer += 1
        minn = score[i]
print(answer)