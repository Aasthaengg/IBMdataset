#!/usr/bin/env python3

def main():
    A,B = map(int, input().split())
    max_val = max(A+B,A-B,A*B)
    print(max_val)



if __name__ == "__main__":
    main()
