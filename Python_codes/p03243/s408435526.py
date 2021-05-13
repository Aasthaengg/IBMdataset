def main():
    N = int(input())
    divide = N // 111
    rest = N % 111
    if rest > 0:
        print((divide+1)*111)
    else:
        print(divide*111)
main()  