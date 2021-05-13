N = int(input())
sub_yes = 0
max_yes = 0
for i in range(N):
    d1,d2 = map(int,input().split())
    if d1 == d2:
        sub_yes += 1
        if sub_yes > max_yes:
            max_yes = sub_yes
    else:
        if sub_yes > max_yes:
            max_yes = sub_yes
        sub_yes = 0
if max_yes >= 3:
    print("Yes")
else:
    print("No")