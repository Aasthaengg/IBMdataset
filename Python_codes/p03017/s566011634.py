n,a_start,b_start,a_goal,b_goal = map(int,input().split())
s = input()

no_rock_double = True
for i in range(a_start, max(b_goal,a_goal)):
    if i+1 < n:
        if s[i] == '#' and s[i+1] == '#':
            no_rock_double = False
can_switch = False
if a_goal > b_goal:
    for i in range(b_start-1, b_goal):
        if s[i - 1:i + 2] == "...":
            can_switch = True
    if no_rock_double and can_switch:
        print('Yes')
    else:
        print('No')
else:
    if no_rock_double:
        print('Yes')
    else:
        print('No')

