inp=list(map(int,input().split()))
l = [0] * 100
for i in inp:
    l[i-1]+=1
if 2 in l:
    print(2)
elif 3 in l:
    print(1)
else:
    print(3)