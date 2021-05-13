def main():
    s = list(input())
    f = s[0]
    for i in range(1, len(s)):
        if f == s[i]:
            print('Bad')
            break
        f = s[i]
    else:
        print('Good')

if __name__ == '__main__':
    main()