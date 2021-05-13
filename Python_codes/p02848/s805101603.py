N = int(input())
S = list(input())
for i in range(len(S)):
    index = ((ord(S[i]) + N) - 65) % 26 + 65
    print(chr(index), sep='', end='')