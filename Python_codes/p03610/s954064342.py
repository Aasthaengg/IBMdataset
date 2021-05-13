s = input()
s_odd = ""

for i in range(1, len(s)+1, 2):
    s_odd += s[i-1]

print(s_odd)