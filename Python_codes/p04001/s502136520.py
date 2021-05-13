import itertools
S = list(input())
ans = []
a = S[0]
pl = ["+",""]

for i in itertools.product(pl, repeat=len(S)-1):
    for j in range(len(S)-1):
        a += i[j]+S[j+1]
    ans.append(eval(a))
    a = S[0]

print(sum(ans))