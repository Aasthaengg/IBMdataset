n=int(input())
h=list(map(int,input().split()))

#ダメなパターンは以下の二つ
#２以上下がる
#連続して1ずつ下がる
import sys
flg=0
for i in range(n-1):
  if h[i+1]-h[i]<=-2:
    print("No")
    sys.exit()
  elif h[i+1]-h[i]==-1 and flg==1:
    print("No")
    sys.exit()
  elif h[i+1]-h[i]==-1 and flg==0:
    flg=1
  elif h[i+1]-h[i]!=0:
    flg=0
print("Yes")
