n = int(input())
s = input()
t = input()

count = 0
for i in range(len(s)):
    if s[i:] != (t[:~i+1] if i > 0 else t):
        count += 1
    else:
        break

print(n + count)
