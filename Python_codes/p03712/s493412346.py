H, W = map(int, input().split())
a = [input() for _ in range(H)]

print("#" * (W + 2))

for a in a:
    print("#"+ a +"#")
print("#" * (W + 2))