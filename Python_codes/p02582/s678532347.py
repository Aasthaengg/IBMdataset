s = input()
d = 0

if s == "RRR":
    d = 3
elif s in {"RRS", "SRR"}:
    d = 2
elif s in {"RSR", "RSS", "SSR", "SRS"}:
    d = 1
else:
    d = 0

print(d)
