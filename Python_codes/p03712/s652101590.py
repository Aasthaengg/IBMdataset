h,w=map(int,input().split())
a=[[] for i in range(h)]
for i in range(h):
    a[i].append(input())
b=["#" for i in range(w+2)]
a.append(b)
a.insert(0,b)

for i in range(h):
    a[i+1].append("#")
    a[i+1].insert(0,"#")
    
for i in range(h+2):
    print("".join(a[i]))
