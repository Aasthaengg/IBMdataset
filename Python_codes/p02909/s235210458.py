import sys
import itertools
wether = input()
if not ( wether == 'Sunny' or wether == 'Cloudy' or wether == 'Rainy'): sys.exit()

base = ['Sunny','Cloudy','Rainy']
print(base[base.index(wether)+1]) if wether != base[-1] else print(base[0])