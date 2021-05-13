S = input()
A = []
down = [] # index
Asum = 0

for i, line in enumerate(S):
    if line == "\\":  # "\"
        down.append(i)
    elif line == "/" and down:
        j = down.pop()
        temp = i - j
        Asum += temp
        while A and A[-1][0] > j:
            temp += A.pop()[1]
        A.append([j, temp])

print(Asum)
print(len(A), *[S for i, S in A])
