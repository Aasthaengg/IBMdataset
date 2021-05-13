N = int(input())
S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
ans = ''
for s in S:
    next = (alphabet.index(s)+N) % 26
    ans += alphabet[next]
print(ans)
