# -*- coding: utf-8 -*-

def main():

    N = int(input())

    ans = 0

    for i in range(1, N+1):
        if i % 2 == 1:

            count = 0

            for j in range(1, i+1):
                if i % j == 0:
                    count +=1
                if count == 8:
                    ans += 1
        
    print(ans)


if __name__ == "__main__":
    main()