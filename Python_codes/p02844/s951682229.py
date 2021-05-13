import sys
import copy
input = sys.stdin.readline

N=int(input())

S=input()


T=[[0] * 10 for _ in range(30000)]
for i in range(N):
    if i!=0:
        T[i]=copy.deepcopy(T[i-1])
    T[i][int(S[i])]+=1
#print(T)

dic={}
flag=[False]*10
for i in range(N-2):
    if flag[int(S[i])]==True:
        continue
    flag[int(S[i])]=True
    for j in range(i+1,N-1):
        tmp2=copy.deepcopy(T[N-1])
        tmp3=copy.deepcopy(T[j])
        tmp4=""
        for k in range(10):
            if tmp2[k]-tmp3[k]!=0:
                tmp4=S[i]+S[j]+str(k)
                #print(tmp4)
                if tmp4 in dic:
                    pass
                else:    
                    dic[tmp4]=1
           
print(len(dic))
#print(dic)