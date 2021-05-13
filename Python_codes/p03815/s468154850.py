N=int(input())
ans1=N//11*2
ans2=(0<N%11)+(6<N%11)
print(ans1+ans2)