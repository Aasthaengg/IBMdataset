a,b = list(map(int,input().split()))
ls = [a+b,a+a-1,b+b-1]
print(max(ls))