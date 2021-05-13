import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = list(map(int, input().split('/')))
    if s[0] < 2019:
        print("Heisei")
    elif s[0] > 2019:
        print("TBD")
    else:
        if s[1] < 4:
            print("Heisei")
        elif s[1] > 4:
            print("TBD")
        else:
            if s[2] <= 30:
                print("Heisei")
            else:
                print("TBD")
        
if __name__ == '__main__':
    main()