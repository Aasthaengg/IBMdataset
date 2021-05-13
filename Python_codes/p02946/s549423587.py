a,b=[int(x) for x in input().split()]

ans=[i for i in range(b-a+1,b+a)]

print(*ans)