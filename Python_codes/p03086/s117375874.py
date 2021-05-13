S = input()
count = 0
koremade = 0
for i in range(0,len(S)):
    if S[i] in 'ACGT':
        count += 1
        if i == len(S)-1:
           if koremade <= count:
               koremade = count 
    else:
        if koremade <= count:
            koremade = count
        count = 0
print(koremade)