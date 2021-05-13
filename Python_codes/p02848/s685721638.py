n = int(input())
S = input()

for s in S:
    seq = (ord(s) - ord("A") + n) % 26
    print(chr(ord("A")+seq), end="")
