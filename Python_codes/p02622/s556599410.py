S = input()
T = input()
count = 0
n = 0
while n < len(S):
    if S[n] != T[n]:
        count += 1
    n += 1
print(count) 