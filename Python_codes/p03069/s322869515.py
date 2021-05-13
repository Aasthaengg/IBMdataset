n=int(input())
c=input()
w=c.count(".")
b=n-w
#全部黒にする場合
ans1=w
#全部白にする場合
ans2=b
"""
まずi=0とし、iを境に左にある黒の合計と右にある白の合計の最小を求める
"""
ans=ans1
tmp_b=0
tmp_w=w
for i in range(n):
    if c[i]==".":
        tmp_w-=1
    else:
        tmp_b+=1
    tmp_ans=tmp_b+tmp_w
    ans=min(ans,tmp_ans)
print(ans)