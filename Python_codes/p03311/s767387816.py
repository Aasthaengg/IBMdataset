n = int(input())
an = sorted([int(j)-(i+1) for i,j in enumerate(input().split())])
print(sum(abs(i - an[len(an)//2]) for i in an))