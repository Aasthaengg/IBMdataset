from itertools import combinations
n=int(input())
print(n*(n-1)//2-n//2)
for i in combinations(range(1,n + 1),2):
    if i[0]+i[1]!=n-n%2+1:
        print(i[0],i[1])