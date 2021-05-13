def main():
    s = input()
    before = ''
    for v in s:
        if before == v:
            print('Bad')
            exit()
        before = v
    print('Good')
        

if __name__ == '__main__':
    main()