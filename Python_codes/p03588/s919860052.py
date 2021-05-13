n=int(input())
l=sorted([list(map(int,input().split())) for _ in range(n)])
a,b,c=l[0][0],l[-1][0],l[-1][1]
print((a-1)+(b-a+1)+c)