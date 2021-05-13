H,W = map(int,input().split())
x = ["#"*(W+2)]
for _ in range(H):
    a = input().strip()
    a = "#"+a+"#"
    x.append(a)
x.append("#"*(W+2))
for i in range(H+2):
    print(x[i])