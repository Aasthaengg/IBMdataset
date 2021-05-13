N=input()
if len(set(N))==1:
    print(int(N))
else:
    for i in range(111,1110,111):
        if i>=int(N):
            print(i)
            exit()