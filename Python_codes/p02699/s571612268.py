def main():

    S, W = map(int, input().split())
    if W >= S:
        return "unsafe"
    return "safe" 

if __name__ == '__main__':
    print(main())
