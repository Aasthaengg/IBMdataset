NN, MM = list(map(int,input().split()))
ARR = [list(input().split()) for l in range(MM)]

bin = [0]*NN
done = [0]*NN

for ind in range(MM):
    if done[int(ARR[ind][0])-1] == 0:
        if ARR[ind][1] == 'WA':
            bin[int(ARR[ind][0])-1] += 1
        else:
            done[int(ARR[ind][0])-1] = 1

cbin = [x * y for (x,y) in zip(done,bin)]
print(sum(done), sum(cbin))