s = input()
K = int(input())

c = [ord(s1)-ord('a') for s1 in s]
sl = list(s)

for i in range(len(s)):
    if c[i] and 26-c[i] <= K:
        sl[i] = 'a'
        K -= 26-c[i]
sl[len(s)-1] = chr((ord(sl[len(s)-1]) - ord('a') + K) % 26 + ord('a'))

print(''.join(sl))