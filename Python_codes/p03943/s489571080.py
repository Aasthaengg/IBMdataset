# A - キャンディーと2人の子供
def main():
    abc = list(map(int, input().split()))


    if sum(abc) == 2*max(abc):
        print('Yes')
    else:
        print('No')
            

if __name__ ==  "__main__":
    main()