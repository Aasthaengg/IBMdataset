sosuu = [2]
A = 55555
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    for L2 in sosuu:
        if L % L2 == 0:
            break # 素数でないことがわかったらそれ以上ループする必要はない
    else: # break で抜けることがなかったら L は素数（Python 特有の制御構文）
        sosuu.append(L)

a=sosuu

n=int(input())

ans=[]

l=0

for i in a:
  if i%5==1:
    ans.append(str(i))
    l+=1
    
  if l==n:
    break


print(' '.join(ans))