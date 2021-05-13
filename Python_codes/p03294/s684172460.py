n=int(input())
a=list(map(int,input().split()))

a=list(map(lambda x:x-1,a))
print(sum(a))
