# B - ∵∴∵
def main():
    o = list(input())
    d = list(input())

    for i in range(len(o)+len(d)):
        if i % 2 == 0:
            print(o.pop(0), end='')
        else:
            print(d.pop(0), end='')

  
        
if __name__ == '__main__':
    main()