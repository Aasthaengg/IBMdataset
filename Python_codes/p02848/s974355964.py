from string import ascii_uppercase

N = int(input())
S = input()

num2alpha = {i: a for i, a in enumerate(ascii_uppercase)}
alpha2num = {a: i for i, a in enumerate(ascii_uppercase)}

ans = ""
for s in S:
    num = (alpha2num[s] + N) % 26
    ans += num2alpha[num]

print(ans)
