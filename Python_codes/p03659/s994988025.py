N=int(input())
a_list = list(map(int,input().split()))

#累積和を作成
s_list=[0]
sum=0
for i in a_list:
    sum+=i
    s_list.append(sum)

#print(s_list)

target=s_list[-1]//2

tmp1=10**10
for i in range(1,N):
    tmp2=abs(target-s_list[i])
    tmp1=min(tmp1,tmp2)#より小さいほうをtmp1に格納
    if tmp1 == tmp2:
        ans_index=i

#print(ans_index)
print(abs(s_list[-1]-2*s_list[ans_index]))