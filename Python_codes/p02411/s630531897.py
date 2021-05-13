midExam, finalExam, reExam = list(map(int, input().split()))
addedResult = midExam + finalExam

while True :
    if midExam == -1 and finalExam == -1 and reExam == -1 :
        break;
    
    if midExam == -1 or finalExam == -1 or addedResult < 30 :
        print("F")
    elif addedResult >= 80 :
        print("A")
    elif addedResult >= 65 and addedResult < 80 :
        print("B")
    elif addedResult >= 50 and addedResult < 65 :
        print("C")
    elif addedResult >= 30 and addedResult < 50 :
        if reExam >= 50 :
            print("C")
        else :
            print("D")
    midExam, finalExam, reExam = list(map(int, input().split()))
    addedResult = midExam + finalExam