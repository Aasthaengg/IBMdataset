S = input()
K = int(input())
Ans = []

while len(Ans) < K:
    for i in range(26):
        if chr(97+i) in S and chr(97+i) not in Ans:
            f = chr(97 + i)
            Ans.append(f)
            break

    for i, s in enumerate(S):
        if s == f:
            for j in range(2, 2 + 10):
                if i + j > len(S):
                    break
                if S[i:i+j] not in Ans:
                    Ans.append(S[i:i+j])
    Ans.sort()
print(Ans[K-1])


