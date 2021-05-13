n = int(input())
l = list(map(int,input().split()))
div = (n//2)-1
l.sort()
print(l[div+1]-l[div])