S = input()

acgt = ['A', 'C', 'G', 'T']


max_l = 0

for i in range(len(S)):
    l = 0
    for j in range(i, len(S)):
        if S[j] in acgt:
            l+=1
        else:
            break
    if l > max_l:
        max_l = l
print (max_l)
