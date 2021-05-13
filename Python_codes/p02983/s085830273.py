from itertools import combinations

l,r = map(int, input().split())

if r//673 > (l-1)//673 and r//3 >(l-1)//3:
  print('0')

else:
    cmb = list(combinations(range(l, r+1), 2))
    mod = [(cmb[i][0] * cmb[i][1]) % 2019 for i in range(len(cmb))]
    print(min(mod))