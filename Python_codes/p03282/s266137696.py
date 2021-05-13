def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    S = input()
    K = ii()
    for i in range(min(len(S), K)):
        if S[i] != '1':
            print(S[i])
            return
    print(1)

if __name__ == '__main__':
    main()