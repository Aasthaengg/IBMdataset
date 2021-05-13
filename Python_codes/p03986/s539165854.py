def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    x = input()            
    cnt  = 0
    t = 0
    for i in x:
        if i == 'S':
            cnt += 1
        else:
            cnt -= 1
        t = min(t, cnt)
    print(cnt-2*t)



if __name__ == '__main__':
    main()