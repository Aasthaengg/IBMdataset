def main():
    n = list(str(input()))
    ans = ''
    for i in n:
        if i == '1':
            ans = ans + '9'
        else:
            ans = ans + '1'
    print(int(ans))
main()