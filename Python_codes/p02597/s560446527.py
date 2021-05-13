n=int(input())
c=input()
a=c.count('R')
print(a-c[:a].count('R'))