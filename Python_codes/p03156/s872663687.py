n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
t1 = len([1 for i in p if i<=a])
t2 = len([1 for i in p if a < i and i <= b])
t3 = len([1 for i in p if i > b])
print(min(t1,t2,t3))