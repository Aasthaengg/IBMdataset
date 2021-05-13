A=[int(input()) for _ in range(5)]
ceiled=[(x+9)//10*10 for x in A]
can_save=[y-x for x,y in zip(A,ceiled)]
ans=sum(ceiled)-max(can_save)
print(ans)