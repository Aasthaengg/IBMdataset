H,W=map(int,input().split())

ans=0       # 裏の数

# 1*1
if H==1 and W==1:
    ans+=1

# 4隅以外の端
if W<2 and H>=3:
    ans+=(H-2)
if H<2 and W>=3:
    ans+=(W-2)

# 上記以外
if H>=3 and W>=3:
    ans+=(H-2)*(W-2)

print(ans)