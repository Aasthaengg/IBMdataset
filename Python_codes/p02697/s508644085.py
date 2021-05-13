#!/usr/bin/python3

(n, m) = map(int, input().split())

if m % 2 == 1:
    #first half
    c = m // 2
    for i in range(c):
        print(i + 1, c * 2 + 1 - i)
        
    #second half
    f = (m // 2) * 2 + 2
    c = m // 2 + 1
    for i in range(c):
        print(f + i, f + c * 2 - 1 - i)
              
else:
    #first half
    c = m // 2
    for i in range(c):
        print(i + 1, c * 2 + 1 - i)
    #second half
    f = (m // 2) * 2 + 2
    c = m // 2
    for i in range(c):
        print(f + i, f + c * 2 - 1 - i)
