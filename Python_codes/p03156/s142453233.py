n=int(input())
a,b=map(int, input().split())
p=list(map(int, input().split()))

first=[i for i in p if i <= a]
second=[i for i in p if i <= b and i >= a+1]
third=[i for i in p if i >=b+1]

print(min(len(first), len(second), len(third)))