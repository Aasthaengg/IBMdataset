n=int(input())
A=[int(i) for i in input().split()]

L=[0 for i in range(n+1)]
for num in A:
    L[num]+=1

big=0
for num in L:
    big+=num*(num-1)//2

for num in A:
    sma=L[num]
    print(big-sma*(sma-1)//2+(sma-1)*(sma-2)//2)