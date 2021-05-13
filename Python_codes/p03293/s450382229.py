S,T=input(),input()
for i in range(len(T)):
    if S==T:print('Yes');exit()
    S=S[-1]+S[0:-1]
print('No')