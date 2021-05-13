l = map(int, raw_input().split())


if l[0] < l[1]:
    output_line = "a < b"
elif l[0] > l[1]:
    output_line = "a > b"
else:
    output_line = "a == b"

print(output_line)