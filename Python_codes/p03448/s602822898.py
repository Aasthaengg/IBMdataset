def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    l = []
    cnt = 0

    for i in range(C+1):
        for j in range(B+1):
            for k in range(A+1):
                if 50*i + 100*j + 500*k == X:
                    if not [i, j, k] in l:
                        cnt += 1
    print(cnt)
main()