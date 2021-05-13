s = input()
t = input()
s_len = len(s)
count = 0
if s == t:
    print("0")
    exit()
else:
    for i in range(s_len):
        if s[i] != t[i]:
            count += 1
        else:
            continue
print(count)