#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

days = {"SUN":7,"MON":6,"TUE":5,"WED":4,"THU":3,"FRI":2,"SAT":1}
def main():
    s = input()
    print(days[s])


if __name__ == '__main__':
    main()
