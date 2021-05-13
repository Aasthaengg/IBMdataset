def hantei(s):
    return len(s) == len(set(s))

def main():
    s = input()
    s = list(s)

    if hantei(s) == True:
        print('yes') 
    else:
        print('no')
        
if __name__ == '__main__':
    main()