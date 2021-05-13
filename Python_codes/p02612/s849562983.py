def main():
    from sys import stdin

    readline = stdin.readline

    N = int(readline().rstrip())
    
    result = ( 10000 - N )%1000

    print(result)

main()