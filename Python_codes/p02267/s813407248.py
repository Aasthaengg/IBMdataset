# -*- coding: utf-8 -*-


def main():
    s_length = raw_input()
    s = set(raw_input().strip().split(' '))
    t_length = raw_input()
    t = set(raw_input().strip().split(' '))

    print len(s.intersection(t))

if __name__ == '__main__':
    main()