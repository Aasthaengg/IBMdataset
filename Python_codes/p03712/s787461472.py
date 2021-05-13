# B - Picture Frame
def main():
    h, w = map(int, input().split())

    for i in range(h):
        a = input()

        if i == 0:
            print(('#'*w)+'##')
            print('#'+a+'#')
        else:
            print('#'+a+'#')
    else:
        print(('#'*w)+'##')


if __name__ ==  "__main__":
    main()