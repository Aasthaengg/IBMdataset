S = input()

result = "Good"
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        result = "Bad"
        break
print(result)