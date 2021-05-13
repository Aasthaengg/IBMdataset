from collections import Counter
# from fractions import gcd # >=Python3.5 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # <Python3.5
# from math import sqrt

# input = sys.stdin.readline
# def main():

#---------------------------------------------------------

n = int(input())

clist = [''.join(sorted(input())) for _ in range(n)]

c = Counter(clist)

print(sum([v*(v-1)//2 for v in c.values()]))