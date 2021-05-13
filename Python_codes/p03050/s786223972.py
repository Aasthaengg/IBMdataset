n=int(input())
print(sum([n//x-1 for x in range(1,int(n**.5)+1) if n%x==0 and n//x-1>x]))