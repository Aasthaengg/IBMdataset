S = input()
before = ''
b = 0
c = 0
for i in range(1, len(S)+1):
    if S[b:i] != before:
        before = S[b:i]
        b =i
        c += 1
print(c)

