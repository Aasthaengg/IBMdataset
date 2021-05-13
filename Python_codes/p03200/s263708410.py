S = input().strip()
l=len(S)
motomoto=0
b=S.count('B')
saisyuu=((2*l-b-1)*b)//2
for i in range(l):
    if S[i]=='B':
        motomoto+=i
print(saisyuu-motomoto)