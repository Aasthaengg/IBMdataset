h, w = (int(i) for i in input().split())
image = ["#" + input() + "#" for _ in range(h)]

print("#" * (w + 2))
print("\n".join(image))
print("#" * (w + 2))