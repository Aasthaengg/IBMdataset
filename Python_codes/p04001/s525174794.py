import copy
S = list(input())
L = len(S)-1 #長さ
tmp = 1
ans = 0
locate = copy.deepcopy(S)
for i in range (2**L):
    for j in range(L):
        if (i >> j) & 1:
            locate.insert(j+tmp,'+')
            tmp += 1 
    locateSTR = "".join(locate)
    ans += (eval(locateSTR))
    tmp = 1
    locate = copy.deepcopy(S)
    
print(ans)