input()
S, T = input().split()

result = ''
for index, s in enumerate(S):
    result += s + T[index]

print(result)
