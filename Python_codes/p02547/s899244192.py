amt = int(input())
same = 0

while amt > 0:
    item = list(map(int, input().split()))
    if item[0] == item[1]:
        same += 1
        if same == 3:
            print("Yes")
            amt = 0
    else:
        same = 0
    amt -= 1

if amt == 0:
    print("No")