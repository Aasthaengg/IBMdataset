S = input()
length = len(S)

num = length//2
counter = 0
for i in range(num):
    if not S[i]==S[-i-1]:
        counter += 1

print(counter)