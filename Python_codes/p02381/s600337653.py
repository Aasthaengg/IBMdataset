#!/usr/bin/env python

if __name__ == '__main__':
    while True:
        n = int(raw_input())
        if n == 0:
            break

        s = map(float, raw_input().split())
        m = sum(s)/len(s)
        print (sum(map(lambda x : (x-m)**2, s))/len(s))**0.5

