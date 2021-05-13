while True:
    a = list(map(int, input().split()));
    if (a[0] == -1) and (a[1] == -1) and (a[2] == -1):
        break;
    if a[0] == -1 or a[1] == -1:
        print('F');
    elif a[0] + a[1] >= 80:
        print('A');
    elif a[0] + a[1] < 80 and a[0] + a[1] >= 65:
        print('B');
    elif a[0] + a[1] < 65 and a[0] + a[1] >= 50:
        print('C');
    elif a[0] + a[1] < 50 and a[0] + a[1] >= 30 and a[2] >= 50:
        print('C');
    elif a[0] + a[1] < 50 and a[0] + a[1] >= 30:
        print('D');
    elif a[0] + a[1] < 30:
        print('F');
