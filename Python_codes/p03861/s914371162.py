# B - Between a and b ...
def main():
    a, b, x = map(int, input().split())

    if a == 0:
        print(b//x+1)
    else:
        print(b//x-((a-1)//x))
            

if __name__ ==  "__main__":
    main()