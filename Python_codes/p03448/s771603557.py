A,B,C,X = (int(input()) for X in range(0,4))
Count = 0
for TA in range(0,A+1):
    for TB in range(0,B+1):
        for TC in range(0,C+1):
            if 500*TA+100*TB+50*TC==X:
                Count += 1
print(Count)