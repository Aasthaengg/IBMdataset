N = input()
if (N[0] == N[1]) and (N[1]==N[2]) and (N[2]==N[0]):
    print(N)
elif int(N[0]) == int(N[1]) and int(N[1]) > int(N[2]):
    print(N[0]*3)
elif int(N[0]) > int(N[1]):
    print(N[0]*3)
else:
    print(str(int(N[0])+1)*3)