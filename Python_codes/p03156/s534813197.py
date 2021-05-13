n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
one=[i for i in p if i<=a]
two=[i for i in p if a<i<=b]
three=[i for i in p if i>b]
print(min(len(one),len(two),len(three)))