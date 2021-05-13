s = input()
n = len(s)
item = []
for i in range(n-2):
    item += [abs(int(s[i:i+3])-753)]

print(min(item))