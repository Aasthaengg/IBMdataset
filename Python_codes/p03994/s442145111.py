S = input()
K = int(input())

def ctoi(c):
    return ord(c) - ord('a')
def toa(c):
    i = ctoi(c)
    return (26-i)%26

ans = ''
for c in S:
    if len(ans)+1 == len(S):
        ans += chr((ctoi(c) + K)%26 + ord('a'))
    else:
        to = toa(c)
        if to <= K:
            ans += 'a'
            K -= to
        else:
            ans += c
print(ans)