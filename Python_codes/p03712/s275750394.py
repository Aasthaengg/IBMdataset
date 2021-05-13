h, w = map(int, input().split())
print("#"*(w+2))
for i in range(h):
    s = input()
    n = "#" + s + "#"
    print(n)
print("#"*(w+2))
