h,ｗ = map(int,input().split())
li = ["#" * (w+2)] + ["#" + input() + "#" for _ in range(h)] + ["#" * (w+2)]

for i in li:
    print(i)