H, W = map(int, input().split())
lis = ["#" + input() + "#" for _ in range(H)]
s = "#" * (W+2)

lis.append(s)
lis.insert(0, s)

for i in lis:
    print(i)