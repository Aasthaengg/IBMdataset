h, w = [int(w) for w in input().split()]
field = [list(input()) for _ in range(h)]

print("#" * (w + 2))
for f in field:
    print(f"#{''.join(f)}#")
print("#" * (w+2))
