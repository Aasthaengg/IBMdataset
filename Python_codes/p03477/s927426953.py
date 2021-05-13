#!/usr/bin/env python3

def main():
    #n = int(input())
    #i = list(map(int,input().split()))
    #j = list(map(int,input().split()))

    a,b,c,d = map(int,input().split())

    if a+b == c+d :
        print('Balanced')
    elif a+b < c+d :
        print('Right')
    else:
        print('Left')

main()
