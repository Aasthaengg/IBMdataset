seq = map(int,raw_input().split())

for i in range(len(seq)):
    for j in range(i,len(seq)-1):
        if seq[i] > seq[j+1]:
            a = seq[j+1]
            seq[j+1] = seq[i]
            seq[i] = a
        
print seq[0],seq[1],seq[2]