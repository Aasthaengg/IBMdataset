def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    if any([a % 2 != 0 for a in A]):
        print('first')
    else:
      	print('second')
        
if __name__ == '__main__':
    main()
