S=input()
L=len(S)//2-1
while S[:L]!=S[L:2*L]:
    L-=1
print(2*L)