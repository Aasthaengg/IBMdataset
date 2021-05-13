#!/usr/bin/env python3
s = input()
K = int(input())
substr= []
for i in range(1, K + 1):
    for k in range(len(s) - i + 1):
        substr.append(s[k: k + i])
substr = sorted(list(set(substr)))
print(substr[K - 1])