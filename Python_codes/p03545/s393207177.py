A,B,C,D = list(input().strip())
if int(A)+int(B)+int(C)+int(D) == 7:
    print(A+"+"+B+"+"+C+"+"+D+"=7")
elif int(A)+int(B)+int(C)-int(D) == 7:
    print(A+"+"+B+"+"+C+"-"+D+"=7")
elif int(A)+int(B)-int(C)+int(D) == 7:
    print(A+"+"+B+"-"+C+"+"+D+"=7")
elif int(A)+int(B)-int(C)-int(D) == 7:
    print(A+"+"+B+"-"+C+"-"+D+"=7")
elif int(A)-int(B)+int(C)+int(D) == 7:
    print(A+"-"+B+"+"+C+"+"+D+"=7")
elif int(A)-int(B)+int(C)-int(D) == 7:
    print(A+"-"+B+"+"+C+"-"+D+"=7")
elif int(A)-int(B)-int(C)+int(D) == 7:
    print(A+"-"+B+"-"+C+"+"+D+"=7")
elif int(A)-int(B)-int(C)-int(D) == 7:
    print(A+"-"+B+"-"+C+"-"+D+"=7")
