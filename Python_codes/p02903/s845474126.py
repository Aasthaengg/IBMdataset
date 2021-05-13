def main():
    H, W, A, B = map(int, input().split())
    l1 = [0]*A + [1]*(W-A)
    l2 = [1]*A + [0]*(W-A)
    s1 = ''.join(map(str, l1))
    s2 = ''.join(map(str, l2))
    for i in range(B):
        print(s1)
    for i in range(B, H):
        print(s2)

if __name__ == '__main__':
    main()
