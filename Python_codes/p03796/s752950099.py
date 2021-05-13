n=int(input())
i=1
j=1
while j!=n+1:
    i=(i*j)%(10**9+7)
    j+=1
print(i)