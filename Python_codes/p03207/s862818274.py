n=int(input())

p=[int(input()) for i in range(n)]
pm=max(p)
c=sum(p)-pm//2
print(c)