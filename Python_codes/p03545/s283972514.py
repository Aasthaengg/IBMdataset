def main():
    import sys
    a = input()
    ans =0
    for i in range(2**3):
        t = a[0]
        for j in range(3):
            if i & (1 <<j):
                t = t +'+'
            else:
                t = t +'-'
            t = t +a[j+1]
        ans =eval(t)
        if ans == 7:
            print(t+'=7')
            sys.exit()
if __name__ =='__main__':
    main()
