input()
a=[*map(int,input().split())]
l=[*map(abs,a)]
print(sum(l)-sum(i<0 for i in a)%2*min(l)*2)