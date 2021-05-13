ab=[]
for _ in range(3):
    a,b = map(int,input().split())
    ab.append(a)
    ab.append(b)
for i in range(1,5):
    if ab.count(i)>=3:
        print("NO")
        exit()
print("YES")
