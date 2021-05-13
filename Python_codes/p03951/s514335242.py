N = int(input())
s = input()
t = input()

for i in range(N):
    if s[i:] == t[:N-i]:
        break
else:
    i += 1
print(N + i)
