if __name__ == '__main__':
    a, b = map(int, input().split())

    print("#"*(b+2))
    for i in range(a):
        s = "#"+input()+"#"
        print(s)

    print("#"*(b+2))


