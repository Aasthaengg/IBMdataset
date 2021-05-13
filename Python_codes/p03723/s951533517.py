member = list(map(int, input().split()))

def check_odd():
    for m in member:
        if m % 2 != 0:
            return True
    return False

def check_number():
    num = member[2]
    for i in range(2):
        if num != member[i]:
            return True
    return False

if check_number():
    count = 0
    while True:
        if check_odd():
            break
        else:
            a = member[1] // 2 + member[2] // 2
            b = member[0] // 2 + member[2] // 2
            c = member[0] // 2 + member[1] // 2
            member = [a, b, c]
        count += 1
    print(count)
else:
    if check_odd():
        print(0)
    else:
        print(-1)