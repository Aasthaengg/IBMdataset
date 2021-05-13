while(True):
    num_in = list(map(int, [i for i in input()]))
    if(num_in[0]==0):
        break
    else:
        print(sum(num_in))

