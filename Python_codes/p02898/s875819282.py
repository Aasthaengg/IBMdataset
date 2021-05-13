#!/usr/bin/env python3

def main():
    N,K = map(int, input().split())
    hights = [int(s) for s in input().split()]
    
    count = 0
    for hight in hights:
        if hight >= K:
            count+= 1
    
    print(count)

if __name__ == "__main__":
    main()
