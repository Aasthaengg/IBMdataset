def binarytruck(maxweight,truck,num):
    disp = 0
    for n in range(num):
        if maxweight - targ[n] - disp < 0:
            disp = targ[n]
            truck -= 1
        else:
            disp += targ[n]
    return truck > 0
num,truck = (int(n) for n in input().split(' '))
global targ
targ = []
for n in range(num):
    targ.append(int(input()))
best = max(targ) - 1
worst = sum(targ)
maxweight = (best + worst ) // 2
cnt = 0
while best != worst - 1:
    cnt += 1
    if binarytruck(maxweight,truck,num):
        worst = maxweight
        maxweight = (best + maxweight) // 2

    else:
        best = maxweight
        maxweight = (worst + maxweight) // 2
print(worst)