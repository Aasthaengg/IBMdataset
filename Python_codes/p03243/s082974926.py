N = int(input())

i=0
while True:
    listN = list(str(N))
    #print(listN)
    if listN[0]==listN[1] and listN[1]==listN[2]:
        print(N)
        break
    N+=1