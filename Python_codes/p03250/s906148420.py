l=list(map(int,input().split()))
l.sort(key=int)
print(int(str(l[-1])+str(l[-2]))+l[0])