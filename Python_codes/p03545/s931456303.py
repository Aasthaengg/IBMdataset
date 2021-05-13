# coding: utf-8

def main():
    S = list(input())

    for i in range(8):
        s = S[0]
        tmp = int(s)

        for j in range(3, 0, -1):
            t = S[4-j]
            if i & 1 << j - 1:
                tmp += int(t)
                s += '+' + t
            else:
                tmp -= int(t)
                s += '-' + t

        if tmp == 7:
            print(s, '=7', sep='')
            break

if __name__ == "__main__":
    main()
