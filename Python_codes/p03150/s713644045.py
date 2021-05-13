s = input()
rev_s = s[::-1]

key = "keyence"
label = [[key[:i], key[i:][::-1]] for i in range(len(key)+1)]

flag = False
for i, l in enumerate(label):
  if s[:i] == l[0] and rev_s[:len(l[1])] == l[1]:
    flag = True
    break
print("YES" if flag else "NO")