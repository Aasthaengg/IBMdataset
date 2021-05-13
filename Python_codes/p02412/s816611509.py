while True:
    ins = list(map(int, input().split()))
    ls = range(1,ins[0]+1)
    
    if ins[0] == 0 and ins[1] == 0:
        break
        
    else:
        counter = 0
        for i in range(ins[0]-2):
           for j in range(i+1, ins[0]-1):
            for k in range(j+1, ins[0]):
                if ls[i] + ls[j] + ls[k] == ins[1]:
                    counter += 1
    print(counter)