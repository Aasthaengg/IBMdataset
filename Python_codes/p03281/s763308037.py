def main():
    n = int(input())
    count = 0
    x_list =[3**3*5, 3**3*7, 3*5*7, 3*5*11, 3*5*13]
    for one in x_list:
        if one<=n:
            count+=1
    print(count)

if __name__=="__main__":
    main()
