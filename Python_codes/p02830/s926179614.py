N = int(input())
S,T = list(map(str,input().split()))
l =[]
for i in range(N):
    l.append(S[i])
    l.append(T[i])
print(''.join(map(str,l)))