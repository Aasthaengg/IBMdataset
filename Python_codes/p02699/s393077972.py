def main():
    S, W = map(int, input().split(' '))
    if S > W:
        print('safe')
    else:
        print('unsafe')
main()