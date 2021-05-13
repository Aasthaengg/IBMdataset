def main():
    date = list(str(input()))
    date[3] = '8'
    ans = ''
    for i in date:
        ans = ans + i
    print(ans)

main()