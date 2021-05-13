n,k = map(int,input().split())
a_input = list(map(int,input().split()))

'''
k=4,a_input=[5,2,4,1]の場合を考える
5 2 4 1 5 2 4 1 5 2 4 1 5 2 4 1 

例えば、4に着目すると
5 2 [4] <1> |5 <2> 4 <1> |5 <2> 4 <1> |5 <2> 4 <1>
1 + 2 + 2 + 2
1 + 2 + 2
1 + 2
1 + 0
で総数を求めることができる
左側の1は(a内の右側でa_i>a_jの個数)*k

それ以外は等差数列の和として
(初項+最終項)*項数/2
= n*(k-1)*k/2
で求めることができる

あとは各数字ごとにこれを足し合わせる
'''
ans=0
for i in range(n):
    tmp1=0#内部の個数
    tmp2=0#a列全体の個数
    for j in range(n):
        if i==j:
            continue
        if j>=i+1:
            if a_input[i]>a_input[j]:
                tmp1+=1
        if a_input[i]>a_input[j]:
            tmp2+=1
    ans+=tmp1*k
    ans+=tmp2*(k-1)*k//2
print(ans%(10**9+7))