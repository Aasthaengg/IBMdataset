def solve():
    s = list(input())
    K = int(input())

    for i in range(len(s)):
        distToA = (ord('z')+1 - ord(s[i])) % 26
        if distToA <= K:
            s[i] = 'a'
            K -= distToA
    else:
        s[-1] = chr(ord(s[-1]) + K%26)
    
    print("".join(s))

if __name__ == '__main__':
    solve()