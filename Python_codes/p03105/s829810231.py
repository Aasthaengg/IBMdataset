#!/usr/bin/env python3
a, b, c = map(int, input().split())
print(c) if a * c <= b else print(int(b / a))
    
