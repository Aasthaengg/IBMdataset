#! -*- coding: utf -*-

import fractions

n = int(input())
monsters = list(map(int, input().split()))

for i in range(n-1):
    monsters[i + 1] = fractions.gcd(monsters[i], monsters[i + 1])

print(monsters[-1])
