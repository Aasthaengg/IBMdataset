n = int(input())
l = list(map(int,input().split()))
l.sort()
print(abs(l[0]-l[len(l)-1]))