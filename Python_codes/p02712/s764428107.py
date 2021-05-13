N=int(input())
i=N//3
j=N//5
k=N//15

sum3=3*i*(1+i)//2
sum5=5*j*(1+j)//2
sum15=15*k*(1+k)//2
sumall=N*(1+N)//2

ans = sumall-(sum3+sum5-sum15)
print(ans)