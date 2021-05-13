T = input()
hatena_count = T.count("?")

pattern = ""
for i in range(hatena_count):
    pattern += "D"

max_exponent = T
for i in range(hatena_count):
    max_exponent = max_exponent.replace("?", pattern[i], 1)

print(max_exponent)
