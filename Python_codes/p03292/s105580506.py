a=sorted([int(i) for i in input().split()])
a=[a[i+1]-a[i] for i in range(len(a)-1)]
print(sum(a))