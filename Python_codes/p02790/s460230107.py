def main():

    a, b = input().split()
    s = a * int(b)
    t = b * int(a)

    if s < t:
        return s
    return t

if __name__ == '__main__':
    print(main())
