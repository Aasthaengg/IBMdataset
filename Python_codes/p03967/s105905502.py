S = input()

p_count = 0

for i in range(len(S)):
    if S[i] == "p":
        p_count += 1

print(int(len(S)/2) - p_count)

