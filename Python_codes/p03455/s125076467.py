

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a, b = map(int, input().split())
    
    if (a * b) % 2 == 0:
        print('Even')
    else:
        print('Odd')
