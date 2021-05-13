import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    month = [i for i in range(1, 13)]
    if int(s[:2]) not in month and int(s[2:]) in month:
        print('YYMM')
    elif int(s[:2]) in month and int(s[2:]) not in month:
        print('MMYY')
    elif int(s[:2]) in month and int(s[2:]) in month:
        print('AMBIGUOUS')
    else:
        print('NA')
    
if __name__ == '__main__':
    main()