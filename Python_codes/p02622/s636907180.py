S=list(input())
T=list(input())


def f(S,T,i):
    if S[i]!=T[i]:
        return 1
    else:
        return 0
sum=0
for i in range(len(S)):
    sum+=f(S,T,i)
print(sum)