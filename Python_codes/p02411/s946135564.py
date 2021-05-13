while True:
    inter_test,end_test,re_test = map(int,raw_input().split())

    if [inter_test,end_test,re_test] == [-1,-1,-1]:
        break
    if inter_test == -1 or end_test == -1 :
        print 'F'
    elif inter_test+end_test >= 80 :
        print 'A'
    elif inter_test+end_test >= 65 :
        print 'B'
    elif inter_test+end_test >= 50 :
        print 'C'
    elif inter_test+end_test >= 30 :
        if re_test >= 50 :
            print 'C'
        else :
            print 'D'
    else :
        print 'F'