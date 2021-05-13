def main():
    n = int(input())
    inlis = list(map(int, input().split()))

    anslis = []
    for _ in range(n):
        anslis.append("")

    if n % 2 == 0:
        for i in range(n):
            if i < n // 2:
                a = -2 * i + n 
            else:
                a = (i - n //2) * 2 + 1
            anslis[i] = inlis[a-1]
    else:
        for i in range(n):
            if i < n // 2:
                a = -2 * i + n
            elif i == n // 2:
                a = 1
            else:
                a = (i - n//2) * 2
            anslis[i] = inlis[a-1]
    print(*anslis)






if __name__ == "__main__":
    main()