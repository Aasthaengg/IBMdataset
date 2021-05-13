a=[int(i) for i in input().split()]
k=int(input())

a.sort()
b=a.pop()
b=b*2**k
a.append(b)
print(sum(a))