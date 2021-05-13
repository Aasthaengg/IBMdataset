N = int(input())
s_rb = input()

counter_R = 0
counter_B = 0
for i in range(N):
    if s_rb[i] == 'R':
        counter_R += 1
    elif s_rb[i] == 'B':
        counter_B += 1

if counter_R > counter_B:
    print('Yes')
else:
    print('No')