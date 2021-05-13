from fractions import gcd


def main():
    s_length, t_length = map(int, input().split())
    s = input()
    t = input()
    lcm = s_length * t_length // gcd(s_length, t_length)
    answer = True
    for i in range(s_length):
        if (i * t_length) % s_length == 0 and s[i] != t[(i * t_length) // s_length]:
            answer = False
            break
    print(lcm if answer else -1)


if __name__ == '__main__':
    main()


