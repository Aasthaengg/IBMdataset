S = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
ex = [0]*26
for i in range(len(S)) :
    index = alpha.index(S[i])
    ex[index] += 1
    if ex[index] != 1 :
        print('no')
        exit()

print('yes')