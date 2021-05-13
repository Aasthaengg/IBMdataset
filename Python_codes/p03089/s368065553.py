#!/usr/bin/env python3

def main():
    N = int(input())
    b = list(map(int,input().split()))

    answer = []
    while b:
        for i in range(len(b)-1,-1,-1):
            if b[i] == i+1:
                answer.append(b[i])
                b.pop(i)
                break
        else:
            print(-1)
            return
    for i in range(N-1,-1,-1):
        print(answer[i])
    return 

if __name__ == '__main__':
    main()
