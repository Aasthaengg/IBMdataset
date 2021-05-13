s = input()
n = [0] * 26
for i in s:
    n[ord(i) - 97] += 1

if 1 in [x % 2 for x in n]:
    print('No')
else:
    print("Yes")
