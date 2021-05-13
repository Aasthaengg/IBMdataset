from collections import defaultdict

h, w = map(int, input().split())
dd = defaultdict(int)
for _ in range(h):
    string = input()
    for s in string:
        dd[s] += 1
        
one = 0
two = 0
for _, value in dd.items():
    if value % 2 == 1:
        one += 1
        value -= 1
    if value % 4 == 2:
        two += 1
        
if h % 2 == 0 and w % 2 == 0:
    if one == two == 0:
        print("Yes")
    else:
        print("No")
elif h % 2 == 1 and w % 2 == 1:
    if one > 1:
        print("No")
    elif two > h // 2 + w // 2:
        print("No")
    else:
        print("Yes")
else:
    if h % 2 == 0:
        tmp = h // 2
    else:
        tmp = w // 2
    if one > 0:
        print("No")
    elif two > tmp:
        print("No")
    else:
        print("Yes")
