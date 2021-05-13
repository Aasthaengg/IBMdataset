def main():
    n = input()[::-1]
    a = 0
    borrow = False
    for i in enumerate(n):
        if i[0] == len(n)-1:
            if borrow:
                a += int(i[1])-1
            else:
                a += int(i[1])
        else:
            if int(i[1]) < 9:
                borrow = True
            a += 9
    print(a)
        
    
if __name__ == "__main__":
    main()