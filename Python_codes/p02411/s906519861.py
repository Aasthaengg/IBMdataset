while True:
    a = input().split(' ')
    if a[0] == '-1' and a[1] == '-1' and a[2] == '-1':
        break
    elif int(a[0]) == -1 or int(a[1]) == -1:
        print('F')
    elif int(a[0]) + int(a[1]) >= 80:
        print('A')
    elif 65 <= int(a[0]) + int(a[1]) < 80:
        print('B')
    elif 50 <= int(a[0]) + int(a[1]) < 65:
        print('C')
    elif 30 <= int(a[0]) + int(a[1]) < 50:
        if int(a[2]) >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')