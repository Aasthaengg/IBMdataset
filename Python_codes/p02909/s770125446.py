import sys
wether = input()
base = ['Sunny','Cloudy','Rainy']

if wether not in base: sys.exit()

print(base[base.index(wether)+1]) if wether != base[-1] else print(base[0])