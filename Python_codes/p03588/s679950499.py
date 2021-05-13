n=int(input())
l=sorted([list(map(int,input().split())) for i in range(n)])
print(l[0][0]-1 + (l[-1][0]-l[0][0]+1) + l[-1][1])