S = input()
L=len(S)
ans=0
S1=S[:(L-1)//2]
S2=S[((L+3)//2)-1:]
if (S==S[::-1]) & (S1==S1[::-1]) & (S2==S2[::-1]):
    ans='Yes'
else:
    ans='No'
print(ans)