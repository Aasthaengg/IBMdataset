#49 ボツ
H,W = map(int,input().split())
a = []
for i in range(H):
    a.append(input())


for i in range(W+2):
    print("#",end = "")
print("")
for i in a:
    print("#",i,"#",sep = "")
for i in range(W+2):
    print("#",end = "")