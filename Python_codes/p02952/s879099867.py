def abc136_b():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    abc136_b()