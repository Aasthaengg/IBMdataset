s = input()

x = list(s)
x.sort()

answer1 = []
answer2 = []

for num in x:
    if len(answer1) == len(answer2):
        answer1.append(num)
    else:
        answer2.append(num)

if answer1 == answer2:
    print('Yes')
else:
    print('No')