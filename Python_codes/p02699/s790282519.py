def main():
    S, W = map(int, input().split())
    print('unsafe') if W >= S else print('safe')
    
    
if __name__ == '__main__':
    main()