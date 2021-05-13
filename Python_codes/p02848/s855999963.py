N = int(input())
S = input()
ans = []

for i in range(len(S)):
    if ord(S[i])+N <= 90:
        ans.append(chr(ord(S[i])+N))
    else:
        ans.append(chr(ord(S[i])+N-26))

print("".join(ans))
