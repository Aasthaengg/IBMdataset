def main():
    data = []
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    div = 0

    one_div=(a == b) and c % a == 0 or c % b == 0

    if one_div:
        div = 1

    for i in range(a, b):
        div_ans = c % i
        if div_ans == 0:
            div += 1

    print(div)

if __name__ == '__main__':
    main()