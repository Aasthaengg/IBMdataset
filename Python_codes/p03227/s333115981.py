# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 土 10/27 21:02:12 2018

# Usage
#
"""
def main():
    IN = input()

    if len(IN) == 2:
        print(IN)

    if len(IN) == 3:
        print(''.join(reversed(IN)))


if __name__ == '__main__':
    main()
