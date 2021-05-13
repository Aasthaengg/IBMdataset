r,D,xs = map(int,input().split())
for i in range(1,11):
    xs = r*xs - D
    print(xs)