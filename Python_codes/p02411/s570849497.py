# Grading

end = 0
while end == 0:
    test = [int(i) for i in input().rstrip().split()]
    midterm = test[0]
    final = test[1]
    makeup = test[2]
    if midterm == -1 and final == -1 and makeup == -1:
        end += 1
    elif midterm == -1 or final == -1:
        print('F')
    else:
        if midterm + final >= 80:
            print('A')
        elif midterm + final >= 65:
            print('B')
        elif midterm + final >= 50:
            print('C')
        elif midterm + final >= 30:
            if makeup >= 50:
                print('C')
            else:
                print('D')
        else:
            print('F')

