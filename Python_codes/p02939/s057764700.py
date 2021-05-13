S = input()
N = len(S)
count = 0
i = 0
last = ""

while i < N:
    if i == 0:
        last = S[i]
        i += 1
        count += 1
    elif i != 0 and last == S[i]:
        if i > N-2:
            break
        last = S[i:i+2]
        i += 2
        count += 1
    elif i != 0 and last != S[i]:
        last = S[i]
        i += 1
        count += 1

if i == N-1 and last != S[N-1]:
    count += 1
print(count)
