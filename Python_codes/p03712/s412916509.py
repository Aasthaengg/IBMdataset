h,w = map(int, input().split())
ab = list(input() for _ in range(h))

header = "#"*(w+2)
print(header)
for i in range(h):
    print("#"+ab[i]+"#")

print(header)