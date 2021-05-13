import collections

def main():
    s = str(input())

    if len(s) % 2 == 0:
        for i in range(len(s)//2):
            if s[0+2*i:2+2*i] != 'hi':
                print('No')
                break
    
        else:
            print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()

