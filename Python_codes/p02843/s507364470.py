x = int(input())

l = -(-x//105)
h = x//100
#fix = l*100

for i in range(l,h+1):
    for b in range(0,i+1):
        for c in range(0,i+1):
            for d in range(0,i+1):
                for e in range(0,i+1):
                    if x - (i*100 + 1*b+2*c+3*d+4*e+5*(i-b-c-d-e)) == 0:
                            print('1')
                            exit()
else:
    print('0')