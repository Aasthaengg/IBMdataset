#payment=桁DPの復習方法
n=input()
#0の方がちょうど、1の方が余裕持って払う
dp0=[0 for i in range(1000002)]
dp1=[0 for i in range(1000002)]
nums=int(n[-1])

dp0[1]=nums
dp1[1]=11-nums
#dp0、dp1でそれぞれぴったり払う時と余裕を持たせて払うときのiけためまでを一つの数としてみたときの最小の値を表すものとする
for i in range(1,len(n)):
    s=int(n[-(i+1)])
    dp0[i+1]=s+min(dp0[i],dp1[i])
    dp1[i+1]=min(9-s+dp1[i],11-s+dp0[i])
print(min(dp0[len(n)],dp1[len(n)]))
