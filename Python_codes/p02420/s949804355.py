# coding: utf-8
while True:
    s = input()
    
    if s == "-":
        break
    
    m = int(input())
    
    for _ in range(m):
        n = int(input())
        s = s[n:] + s[:n]
    
    print(s)