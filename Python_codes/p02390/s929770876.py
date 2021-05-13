S = input()
h = int(S)/3600
S_1 = int(S)%3600
m = int(S_1)/60
s = int(S_1)%60
print('%d:%d:%d'% (h,m,s))
