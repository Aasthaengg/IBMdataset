n,k,s = map(int,input().split())


l = [s+1] * n
if(s == 10**9):l = [1] * n
for i in range(k):l[i] = s

print(' '.join(map(str,l)))