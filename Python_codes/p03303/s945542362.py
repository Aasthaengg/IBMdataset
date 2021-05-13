S = input()
w = int(input())

m = ""
for i in range(0, len(S), w):
    m += S[i]
print(m)