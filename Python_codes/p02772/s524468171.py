def main():
    N=int(input())
    A=list(map(int, input().split()))
    even=[i for i in A if i % 2 == 0]
    for i in even:
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            print('DENIED')
            return
    print('APPROVED')
main()