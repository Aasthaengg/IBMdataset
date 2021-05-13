S=input()

o=['-','+']
for h in o:
    for i in o:
        for j in o:
            if 7 == eval(S[0]+h+S[1]+i+S[2]+j+S[3]):
                print(S[0]+h+S[1]+i+S[2]+j+S[3]+"=7")
                exit()