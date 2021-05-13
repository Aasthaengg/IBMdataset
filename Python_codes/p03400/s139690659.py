_,d,x,*a=map(int, open(0).read().split())
print(sum(~-d//i+1 for i in a)+x)