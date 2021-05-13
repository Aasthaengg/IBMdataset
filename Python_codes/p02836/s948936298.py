def main():
    s = input(); total = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            total += 1
    print(total)
main()