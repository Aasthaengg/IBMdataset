def main():
    n = int(input())
    a = list([(int(input())) % 2 for i in range(n)])
    ans = sum(a)
    if(ans == 0):
        print('second')
    else:
        print('first')

main()