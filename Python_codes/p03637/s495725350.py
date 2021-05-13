N = int(input())
a_list = list(map(int, input().split()))
fours = []
twos = []
others = []

for a in a_list:
    if a % 4 == 0:
        fours.append(a)
    elif a % 2 == 0:
        twos.append(a)
    else:
        others.append(a)

if len(twos) > 0:
    if len(fours) - len(others) < 0:
        print('No')
    else:
        print('Yes')

else:
    if len(fours) - len(others) < -1:
        print('No')
    else:
        print("Yes")