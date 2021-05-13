S = list(input())
Alphabet_list = set(S)
mincnt = 10**5

for letter in Alphabet_list:
    #convert T->Uniform
    cnt = 0
    T = S.copy()
    while(len(set(T)) > 1):
        cnt += 1
        for i in range(len(T)-1):
            if(T[i] == letter or T[i+1] == letter):
                T[i] = letter
            else:
                pass
        del T[-1]
    mincnt = min(mincnt,cnt)
print(mincnt)

