li=list(input())
lis=[]
for i in range(len(li)):
  lis.append(li[i])
  lis.append('')
lis.pop(-1)
sum=0
for i in range(2**(len(li)-1)):
    for j in range(len(li)-1):
      if (i >> j)&1:
          lis[2*j+1]='+'
    str=''.join(lis)
    calc=0
    a=[]
    #計算
    a=list(str.split('+'))
    for j in a:
      calc+=int(j)
    sum+=calc
    #戻す
    for j in range(len(li)-1):
      lis[2*j+1]=''
print(sum)