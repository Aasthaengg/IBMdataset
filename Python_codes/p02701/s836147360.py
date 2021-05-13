# -*- coding: utf-8 -*-

def main():
    n = int(input())
    keihin_list = []
    for i in range(n):
        s = input()
        keihin_list.append(s)
    print(len(set(keihin_list)))

if __name__ == "__main__":
    main()