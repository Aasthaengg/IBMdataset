import sys
K = int(input())
if not (2 <= K <= 100):
    sys.exit()

array_all = [ all for all in range(K) ]
array_even = array_all[0::2]
array_odd = array_all[1::2]

count = 0
for I in array_even:
    for J in array_odd:
        count += 1
print(count)