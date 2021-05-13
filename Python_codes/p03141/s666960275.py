N = int(input())
l=[list(map(int,input().split())) for i in range(N)]
l_after=sorted(((i+j,i,j) for i,j in l),reverse=True)
print(sum(b for a,b,c in l_after[::2])-sum(c for a,b,c in l_after[1::2]))