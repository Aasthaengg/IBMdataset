number = int(input())
score = list(map(int,input().split()))
deny = 0
for i in range(number):
    if score[i] % 2 == 0:
        if score[i] % 3 != 0 and score[i] % 5 != 0:
            deny = 1
            break
if deny == 1:
    print('DENIED')
else:
    print('APPROVED')