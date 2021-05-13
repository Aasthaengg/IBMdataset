def main():
    N, H = (int(_) for _ in input().split())
    S = sorted([[int(_) for _ in input().split()] for __ in range(N)])[::-1]
    output = 0
    for a, b in sorted(S, key=lambda x:-x[1]):
        if b > S[0][0]:
            H -= b
            output += 1
            if H <= 0: break
    if H > 0:
        output += (H+S[0][0]-1)//S[0][0]
    print(output)
    return

if __name__ == '__main__':
    main()
