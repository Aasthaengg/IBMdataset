def main():
    s = input()
    ans = 'no'
    if len(set(s)) == len(s):
        ans = 'yes'
    print(ans)



if __name__ == '__main__':
    main()
