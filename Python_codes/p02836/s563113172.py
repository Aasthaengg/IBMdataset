def main():
    S = str(input())
    n = len(S) // 2
    hug = 0
    for i in range(n):
        if S[i] != S[(i*-1) - 1]:
            hug += 1
    print(hug)
main()