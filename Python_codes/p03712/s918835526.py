h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

print("#"*(w+2))
for i in range(h):
    a[i] = ["#"] + a[i] +["#"]
    print("".join(a[i]))
print("#"*(w+2))
