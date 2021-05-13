r,d,x=[int(x) for x in input().rstrip().split()]
ans=r*x-d
print(ans)
for i in range(9):
    ans=r*ans-d
    print(ans)


