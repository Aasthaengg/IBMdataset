from string import ascii_lowercase
s = input()
k = int(input())

def main(s, k):
    alp = ascii_lowercase
    num = {char: i for i, char in enumerate(alp)}

    ns = [num[char] for char in s]

    for i in range(len(ns)):
        v = ns[i]
        if v != 0 and 26 - v <= k:
            ns[i] = 0
            k -= 26 - v

    ns[-1] = (ns[-1] + k) % 26

    return ''.join(alp[n] for n in ns)
print(main(s, k))