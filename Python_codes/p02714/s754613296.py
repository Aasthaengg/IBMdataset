def main5():
    N = int(input())
    S = list(input())

    r = g = b = 0
    for c in S:
        if c == "R":
            r += 1
        if c == "G":
            g += 1
        if c == "B":
            b += 1

    tmp = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            k = 2*j - i
            if  k < len(S) and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                tmp += 1
    
    ans = r*g*b - tmp

    print(ans)

if __name__ == "__main__":
    main5()