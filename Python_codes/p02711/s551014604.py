score = int(input())
answer = 0
for i in range(3):
    if int(score/(10**i))%10 == 7:
        answer = 1
        break
if answer == 1:
    print('Yes')
else:
    print('No')