N = int(input())
t_before = 0
x_before = 0
y_before = 0

travel_list = [map(int, input().split()) for _ in range(N)]

def judge(t_plus, x_diff, y_diff):
    distance = abs(x_diff) + abs(y_diff)
    if (t_plus % 2) != (distance % 2):
        return False
    if distance > t_plus:
        return False 
    return True

is_found = False

for i in range(N):
    t, x, y = travel_list[i]
    result = judge(t_plus=t-t_before, x_diff=x-x_before, y_diff=y-y_before)
    if result:
        t_before = t
        x_before = x
        y_before = y
    else:
        break
else:
    is_found = True
if is_found:
    print("Yes")
else:
    print("No")

