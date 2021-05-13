NN=raw_input()
N=raw_input()
N = [int(i) for i in N.split()]
print ' '.join([str(k) for k in N])

for i in range(1,int(NN)):
    key = N[i]
    j = i - 1
    while (j >= 0) and (N[j] > key):
        N[j+1] = N[j]
        j=j-1
    N[j+1] = key
    print ' '.join([str(k) for k in N])