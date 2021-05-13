string_list = map(str, raw_input().split(","))

result = [i.swapcase() for i in string_list]
print ",".join(result)