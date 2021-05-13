
def main():
    n = int(input())
    a_s = list(map(int,input().split()))
    dct = {}
    for i,value in enumerate(a_s):
        i = i+1
        dct[i] = value
    counter = 0
    for key in dct.keys():
        if dct[dct[key]] == key:
            counter += 1
    print(counter//2)


if __name__ == '__main__':
    main()
