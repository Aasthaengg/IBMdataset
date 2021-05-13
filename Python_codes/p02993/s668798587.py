password = input()
x = list(password)
if int(x[0])-int(x[1]) == 0 \
    or int(x[1])-int(x[2]) == 0 \
    or int(x[2])-int(x[3]) == 0 :
    print("Bad")
else : print("Good")
