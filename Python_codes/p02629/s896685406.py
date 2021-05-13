N = int(input())

bit = []
while N > 0:
    M = (N-1) % 26
    N = (N-1) // 26
    bit.append(M)

alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
char = []
for i in range(len(bit)):
        char.insert(0, alph[bit[i]])

ans = "".join(char)
print(ans)