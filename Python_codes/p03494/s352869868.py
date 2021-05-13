N = int(input())
Alist = list(map(int, input().split()))
answer = 40
for a in Alist:
    i = 0
    while a % 2 == 0:
        a = a / 2
        i += 1
    if i < answer:
        answer = i
print(answer)
