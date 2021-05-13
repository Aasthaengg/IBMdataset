n = int(input())

for i in range(1000):
    if str(n)[0] == str(n)[1] ==str(n)[2]:
        print(n)
        exit()
    else:
        n+=1