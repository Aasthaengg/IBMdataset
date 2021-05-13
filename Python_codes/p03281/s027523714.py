N = int(input())
xList = [105,135,165,189,195]
answer = 0
for i in xList:
    if i <= N:
        answer += 1
print(answer)
