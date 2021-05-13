d,n = map(int,input().split())
li = []
for i in range(1,102):
    if i != 100:
        li.append(i*100**d)
print(li[n-1])