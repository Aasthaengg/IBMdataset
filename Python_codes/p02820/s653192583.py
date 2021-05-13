n,k = map(int, input().split())
r,s,p = map(int, input().split())
t= input()
T = [i for i in t]

win = ''
for i in range(len(T)-k):
    if T[i]==T[i+k]:
        T[i+k]='#'
ans = 0
for i in T:
    if i=='r':ans+=p
    elif i=='s':ans+=r
    elif i=='p':ans+=s
print(ans)
