N = int(input())
S = list(input())
t1 = S.count('R')
S_R = S[:t1]
t2 = S_R.count('R')
print(t1-t2)