S0='CODEFESTIVAL2016'
S=input()
ans=sum([S[i]!=S0[i] for i in range(len(S0))])
print(ans)