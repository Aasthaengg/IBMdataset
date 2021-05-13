S = input()
K = int(input())
Flag = True
for T in range(0,min(K,len(S))):
    if S[T]!='1':
        Disp = S[T]
        Flag = False
        break
if Flag: print('1')
else: print(Disp)