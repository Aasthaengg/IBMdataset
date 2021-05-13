h, w = map(int, input().split())
a = [input() for _ in range(h)]

print("#"*(w+2))
for a_ in a:
    print("#" + a_ + "#")
print("#"*(w+2))