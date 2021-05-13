A,B,K=map(int,input().split())
A_yaku=[]
B_yaku=[]

for i in range(1,A+1):
    if A % i == 0:
        A_yaku.append(i)

for j in range(1,B+1):
    if B % j == 0:
        B_yaku.append(j)

A_B_and_set = set(A_yaku) & set(B_yaku)
A_B_and_list = list(A_B_and_set)

ans_list=sorted(A_B_and_list,reverse=True)

ans=ans_list[K-1]
print(ans)