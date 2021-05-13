# -*- coding: utf-8 -*-
import math

def search(current, K, count, N):
  if count >= N:
    return current

  a = search(current * 2, K, count + 1, N)
  b = search(current + K, K, count + 1, N)
  return min(a, b)


def main():
  N = int(input())
  K = int(input())
  
  print(search(1, K, 0, N))


if __name__ == '__main__':
  main()
