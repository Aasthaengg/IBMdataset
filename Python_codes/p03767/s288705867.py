n=int(input())*3
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
print(sum(a[1:n//3*2:2]))