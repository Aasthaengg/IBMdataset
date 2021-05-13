n = int(input())
s_array = [input() for x in range(n)]
a_count = 0
b_count = 0
ab_count = 0
for s in s_array:
    if s[-1] == "A" and s[0] != "B":
        a_count += 1
    elif s[0] == "B" and s[-1] != "A":
        b_count += 1
    elif s[0] == "B" and s[-1] == "A":
        ab_count += 1
    else:
        pass

res = sum([x.count("AB") for x in s_array])

if n == 1:
    print(res)
elif ab_count == 0:
    print(res + min(a_count, b_count))
elif a_count == 0 and b_count == 0:
    print(res - 1 + ab_count)
else:
    print(res + min(a_count, b_count) + ab_count)
