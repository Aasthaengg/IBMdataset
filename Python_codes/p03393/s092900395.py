s = input()

used = [0] * 26

for x in s:
    idx = ord(x) % 26
    used[idx] += 1

if len(s) < 26:
    for i in range(97, 97+26+1):
        if not used[i%26]:
            print(s+chr(i))
            exit()

decrease_point = 0
for i in range(len(s)-1):
    if s[i] < s[i+1]:
        decrease_point = i + 1

if decrease_point == 0:
    print(-1)
    exit()

add_chr = s[decrease_point]
for x in s[decrease_point:]:
    if x > s[decrease_point-1] and x < add_chr:
        add_chr = x

print(s[:decrease_point-1] + add_chr)
