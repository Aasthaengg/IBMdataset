N = int(input())
s = input()
t = input()
index = 0
for i in s:
    if i == t[index]:
        index += 1
    else:
        continue
print(len(s + t[index:]))