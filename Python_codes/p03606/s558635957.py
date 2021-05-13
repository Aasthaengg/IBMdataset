n=int(input())
a = [[int(i) for i in input().split()] for l in range(n)]
c=0
for x in a:
    c+=x[1]-x[0]+1
print(c)