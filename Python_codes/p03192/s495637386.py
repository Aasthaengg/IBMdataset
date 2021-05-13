a = int(input())

answer = 0

if a//1000 == 2:
    answer += 1

if (a//100)%10==2:
    answer += 1

if (a//10)%10==2:
    answer += 1

if (a//1)%10==2:
    answer += 1
print(answer)