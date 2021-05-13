def solve():
    S = input()
    l = len(S)
    K = int(input())
    i = 0
    ans = ''
    while i < l-1 and K>0:
        n = ord(S[i])-ord('a')
        if n==0:
            ans += 'a'
            i += 1
            continue
        if 25-n<K:
            ans += 'a'
            K -= 26-n
        else:
            ans += S[i]
        i += 1
    if K == 0:
        ans += S[i:]
    else:
        ans += chr((ord(S[-1])-ord('a')+K)%26+ord('a'))
    return ans
print(solve())