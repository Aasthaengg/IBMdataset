a=sorted([int(i) for i in input().split()])
k=int(input())
a[-1]*=2**k
print(sum(a))