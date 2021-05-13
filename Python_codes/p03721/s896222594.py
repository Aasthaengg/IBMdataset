n,k=map(int, input().split())
ab=[]
for i in range(n):
    a,b=map(int, input().split())
    ab.append((a,b))
ab.sort()
p=0
for i in range(n):
    if k <= p+ab[i][1]:
        print(ab[i][0])
        break
    else:
        p+=ab[i][1]