#!/usr/bin/env python3

alpha = {
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
}

S=set(input())
if len(S) == len(alpha):
    print("None")
else:
    print(sorted(alpha - S)[0])


