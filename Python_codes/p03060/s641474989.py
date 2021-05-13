n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ab=[a[i]-b[i] if a[i]-b[i]>=0 else 0 for i in range(n)]
print(sum(ab))