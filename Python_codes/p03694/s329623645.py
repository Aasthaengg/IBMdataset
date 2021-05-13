N=int(input())
alist=list(map(int,input().split()))
alist.sort()

print(alist[-1]-alist[0])