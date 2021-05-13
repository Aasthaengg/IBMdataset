# C - Go Home
def main():
    x = int(input())
    cnt = 0
    for i in range(x + 1):
        cnt += i
        if cnt >= x:
            print(i)
            exit()
        
if __name__ == '__main__':
    main()