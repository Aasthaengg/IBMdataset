n = list(input())
for i in range(0, len(n)):
    n[i] = "9" if n[i] == "1" else "1"
print(''.join(n))
