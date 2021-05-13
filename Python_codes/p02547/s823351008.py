def judge():
    count = 0
    for _ in range(x):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
        else:
            count = 0
        
        if count == 3:
            return True

    return False

x = int(input())

if judge():
    print("Yes")
else:
    print("No")
