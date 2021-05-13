
def main():
    import math
    x = int(input())

    k_11 = math.ceil(x / 11)
    if 11*k_11 -5 >= x:
        print(2*k_11 - 1)
    else:
        print(2*k_11)




if __name__ == "__main__":
    main()