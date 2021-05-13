N=int(input())
A=[]
r=[]
for i in input().split():
  A.append(int(i))
#入力した配列をソート
A.sort()

#Queue操作
t=A.pop(-1) #最大値をとりだす
#print('t=',t)
b=A.pop(0)  #最小値をとりだす
#print('b=',b)

#残りの配列において
for i in A:
  #print(i)
  #非負の場合
  if i>=0:
    r.append([b,i]) #最小値と現在の値のペア
    b=b-i  #bを更新
  #負の場合
  else:
    r.append([t,i]) #最大値と現在の値のペア
    t=t-i #tを更新
print(t-b)
r.append([t,b])
for i in r:
  #print(i)
  print(i[0],i[1])