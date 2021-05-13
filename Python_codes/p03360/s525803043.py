a=list(map(int,input().split()))
a.sort(reverse=True)
for itr in range(int(input())):
    a[0]*=2
print(sum(a))