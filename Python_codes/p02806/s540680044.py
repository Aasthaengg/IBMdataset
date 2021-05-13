n=int(input())
S=[]
T=[]
time=0
for i in range(n):
    s,t=map(str,input().split())
    S.append(s)
    T.append(int(t))
x=input()
for i in range(50):
    if S[i]==x:
        break
for j in range(i+1,n):
    time+=T[j]
print(time)