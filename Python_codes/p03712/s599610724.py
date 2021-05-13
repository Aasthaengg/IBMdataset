H, W = map(int, input().split())
ma = []

for i in range(H):
    a = [input()]
    a.insert(0,"#")
    a.append("#")
    ma.append(a)

x = "#"*(W+2)

print(x)
for i in range(H):
    print("".join(ma[i]))  
print(x)
     

