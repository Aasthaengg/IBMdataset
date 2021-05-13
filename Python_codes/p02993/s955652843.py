line = list(input())
if line[0] != line[1]:
    if line[1] != line[2]:
        if line[2] != line[3]:
            print("Good")
        else:
            print("Bad")
    else:
        print("Bad")
else:
    print("Bad")