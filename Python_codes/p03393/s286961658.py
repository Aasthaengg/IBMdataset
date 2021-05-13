def solve():
    S = input()
    
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        return -1
    elif len(S) == 26:
        for i in range(26):
            for j in range(ord(S[-i-1])+1, 97+26):
                if chr(j) not in S[:-i-1]:
                    return S[:-i-1] + chr(j)
    else:
        for i in range(97, 97+26):
            if chr(i) not in S:
                return S+chr(i)
            
print(solve())