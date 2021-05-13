
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    all = 0
    for ele in a:
        all ^= ele
    for ele in a:
        print(all ^ ele,end = " ")
    print()



if __name__ == "__main__":
    main()