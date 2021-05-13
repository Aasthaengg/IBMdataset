def main(n):
    if n in [2, 4, 5, 7, 9]:
        return 'hon'
    elif n in [0, 1, 6, 8]:
        return 'pon'
    else:
        return 'bon'

if __name__ == '__main__':
    N = int(input())
    n = N%10
    ans = main(n)
    print(ans)

