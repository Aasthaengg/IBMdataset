a=int(input())
b=[int(input()) for i in range(a)]
b.sort()
c=sum(b)
print(int(c-b[a-1]/2))