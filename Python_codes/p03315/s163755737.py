#!/usr/bin/env python3
s = input()
answer = 0
answer += s.count('+')
answer -= s.count('-')
print(answer)
