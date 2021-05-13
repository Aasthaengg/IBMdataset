n = str(input())
a = ""
for i in range(0, len(n)):
    if i % 2 == 0:
        a += n[i]

print(a)