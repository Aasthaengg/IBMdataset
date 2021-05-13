n=int(input())
marchlist=[0]*5
for i in range(n):
    tmps=input()
    fs=tmps[0]
    if fs == "M":
        marchlist[0] = marchlist[0] + 1
    elif fs == "A":
        marchlist[1] = marchlist[1] + 1
    elif fs == "R":
        marchlist[2] = marchlist[2] + 1
    elif fs == "C":
        marchlist[3] = marchlist[3] + 1
    elif fs == "H":
        marchlist[4] = marchlist[4] + 1
counter=0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            counter += marchlist[i]*marchlist[j]*marchlist[k]
print(counter)