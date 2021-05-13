def main():
    s  = input()
    ind_a = 0
    ind_z = 0
    for i in range(len(s)):
        if(s[i]=="A"):
            ind_a = i
            break
    for i in range(len(s)-1,-1,-1):
        if(s[i]=="Z"):
            ind_z = i
            break



    print(ind_z-ind_a+1)
if __name__ == '__main__':
    main()
