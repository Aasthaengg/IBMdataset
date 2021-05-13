N = int(input())

sousuu = 10 ** N
not9 = 9 ** N
not0 = 9 ** N
not09 = 8 ** N
print((sousuu - not9 - not0 + not09) % (10 ** 9 + 7))