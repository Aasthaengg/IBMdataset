n=int(input())
a=[int(i) for i in input().split()]
aa=[1/i for i in a]
print(1/sum(aa))