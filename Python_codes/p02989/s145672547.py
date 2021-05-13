N=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(max(0,l[int(N/2)] - l[int(N/2)-1]))
