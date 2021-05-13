NN, MM = list(map(int,input().split()))
ARR = [list(map(int,input().split())) for l in range(MM)]
PMAP = list(map(int,input().split()))
#print(NN,MM,ARR)
switch = [[0 for j in range(NN)] for i in range(MM)]
for i in range(MM):
    for j in range(ARR[i][0]):
        switch[i][ARR[i][j+1]-1] = 1
#print(switch)

number_of_switch_on = 0
for j in range(2**NN):
#   print("bit-full-search step ", j)
    switch_on = 1
    for l in range(MM):
        checksum = 0
#        print("Checking Bulb", l+1)
        for k in range(NN):
            if (j>>k) & 1:
#               print("Switch ", k+1, " is on!")
                checksum += switch[l][k]
#        print("Checksum of switch ",l," is", checksum)
        if (checksum % 2) != PMAP[l]:
            switch_on = 0
    number_of_switch_on = number_of_switch_on + switch_on
#    print(" ")
#    print()
print(number_of_switch_on)