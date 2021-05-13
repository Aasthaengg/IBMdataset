
S = str(input())

if S[0] == S[1]:
    result = "Bad"
elif S[1] == S[2]:
    result = "Bad"
elif S[2] == S[3]:
    result = "Bad"
else:
    result = "Good"

print(result)