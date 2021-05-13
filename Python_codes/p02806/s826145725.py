n=int(input())
s,t=[],[]
#s:曲名
#t:再生時間
for i in range(n):
    S,T=input().split()
    s.append(S)
    t.append(int(T))
x=input()
#print(s,t,sep='\n')

wake=0
for a,b in zip(s,t):
    wake+=b
    if a==x:
        print(sum(t)-wake)
        exit()
