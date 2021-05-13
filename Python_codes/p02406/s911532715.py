# -*- coding: utf-8 -*-

import sys
import os



"""
void call(int n){
  int i = 1;
 CHECK_NUM:
  int x = i;
  if ( x % 3 == 0 ){
    cout << " " << i;
    goto END_CHECK_NUM;
  }
 INCLUDE3:
  if ( x % 10 == 3 ){
    cout << " " << i;
    goto END_CHECK_NUM;
  }
  x /= 10;
  if ( x ) goto INCLUDE3;
 END_CHECK_NUM:
  if ( ++i <= n ) goto CHECK_NUM;

  cout << endl;
}
"""

def include3(v):
    s = str(v)
    if '3' in s:
        return True
    else:
        return False

def call(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(" ", end='')
            print(i, end='')
        else:
            if include3(i):
                print(" ", end='')
                print(i, end='')

n = int(input())
call(n)
print()