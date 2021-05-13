# -*- coding: utf-8 -*-

def main():
    N, A, B = map(int, input().split())
    print(['Yes', 'No'] [N + A < B])

if __name__ == '__main__':
    main()