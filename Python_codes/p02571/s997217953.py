# 171 B
S = input()
T = input()
ans = []
for i in range(0, (len(S)-len(T) + 1)):
    tmp = 0
    #print(i)
    for j in range(0, len(T)):
        if T[j] != S[i +j]:
            tmp += 1
            #print(S[i +j] + T[j])
        #print('tmp:' + str(tmp))
    ans.append(tmp)
        
print(min(ans))