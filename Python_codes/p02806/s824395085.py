n=int(input())
S=[]
T=[]
for i in range(n):
    s,t=input().split()
    S.append(s)
    T.append(int(t))
print(sum(T[S.index(input())+1:]))