a,b,x=map(int,input().split())
#メモ
#3-25 5 5個
#5-25 5 5個
#6-25 5 4個

b1=b//x
if a%x==0:
  b1+=1
a1=a//x

print(b1-a1)