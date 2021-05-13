K = int(input())
S = input()

word = S
if len(S) > K:
    word =  S[:K] + "..."
print(word)