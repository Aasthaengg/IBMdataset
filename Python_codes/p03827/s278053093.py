n = int(input())
s = input()

a = [0]
for i in range(n):
    a.append(a[-1]+1 if s[i] == 'I' else a[-1]-1)
print(max(a))