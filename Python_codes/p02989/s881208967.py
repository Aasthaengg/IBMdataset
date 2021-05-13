n = int(input())
d = list(map(int,input().split()))
d.sort()
a = n//2-1
print(d[a+1]-d[a])