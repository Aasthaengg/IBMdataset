S = input()
T = input()

sl = len(S)
tl = len(T)

minc = 1000

for i in range(sl):
    if i+tl-1 >= sl:
        break
    else:
        str1 = S[i:i+tl]
        count=0
        for j in range(tl):
            if str1[j] != T[j]:
                count+=1
        if count < minc:
            minc = count

print(minc)
        




