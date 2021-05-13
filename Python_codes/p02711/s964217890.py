import sys
input = sys.stdin.readline

def main():

    n = str(input())
    for i in range(len(n)):
        if n[i] == '7':
            print('Yes')
            sys.exit()
    print('No')


main()