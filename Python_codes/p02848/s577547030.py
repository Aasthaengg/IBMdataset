N = int(input())
S = input()

for s in S:
    ans = ord(s) + N
    if ans > 90:
        ans -= 26
    print(chr(ans), end='')