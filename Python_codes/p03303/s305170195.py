s = input()
w = int(input())
t = []

for i in range(len(s))[::w]:
    t.append(s[i])

print(''.join(t))