#   OddString

in_s = list(input())

out_ss = ""

for i, new in enumerate(in_s):
    if i % 2 == 0:
        out_ss += new

print(out_ss)
