S=input()
N=len(S)
A=S.count('a')
B=S.count('b')
C=S.count('c')

print('YNEOS'[max([A,B,C])-min([A,B,C])>=2::2])