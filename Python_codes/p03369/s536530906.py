S = input()
S_c = S.count("o")
if(S_c==3):
    print("1000")
elif(S_c==2):
    print("900")
elif(S_c ==1):
    print("800")
else:
    print("700")