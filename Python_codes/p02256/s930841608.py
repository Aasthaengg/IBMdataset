# -*- coding : utf-8 -*-

def gcd(num_a, num_b):
    if num_b == 0:
        return num_a
    elif num_a == 0:
        return num_b

    if num_a < num_b:
        return gcd(num_a, num_b % num_a)
    else:
        return gcd(num_b, num_a % num_b)

num_a, num_b = [int(x) for i, x in enumerate(input().split()) if i < 2]
print(gcd(num_a, num_b))