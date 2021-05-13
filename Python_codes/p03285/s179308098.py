def main():
    total = int(input())
    i = 0
    j = 0

    for i in range(26):
        for j in range(16):
            if total == (i*4 + j*7):
                print('Yes')
                return

    print('No')

main()
