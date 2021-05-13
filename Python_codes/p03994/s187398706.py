def main():
    S = list(input())
    K = int(input())
    k = K
    for i,c in enumerate(S):
        distance = (ord('z') + 1 - ord(c))%26
        if distance <= k:
            k -= distance
            S[i] = 'a'
    S[-1] = chr((ord(S[-1]) - ord('a') + k) % 26 + ord('a'))
    print(''.join(S))

main()