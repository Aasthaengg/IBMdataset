def main():
    N = str(input())
    S = list(map(str, input().split(' ')))
    a = len(set(S))
    if a == 3:
        print('Three')
    elif a == 4:
        print('Four')
main()
