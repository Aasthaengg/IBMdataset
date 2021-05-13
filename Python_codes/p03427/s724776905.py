a=list(input())
p=print
x=len(a)-1
y=int(a[0])
print(9*x+y if all(i=='9' for i in a[1:]) else y-1+9*x)