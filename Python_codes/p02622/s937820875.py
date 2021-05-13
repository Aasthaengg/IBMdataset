S=input()
T=input()
S_list=list(S)
T_list=list(T)
N=len(S_list)
count=0
for i in range(N):
    if S_list[i]!=T_list[i]:
        count=count+1
print(count)