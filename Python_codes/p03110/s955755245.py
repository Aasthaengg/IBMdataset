import sys
N = int(input())
array = [ list(map(str,input().split())) for I in range(N) ]
# print(array)
for I in array:
    if not ( I[1] == 'JPY' and 1 <= int(I[0]) <= 10 ** 8 ) and \
    not ( I[1] == 'BTC' and 1/10 ** 8 <= float(I[0]) <= 100 ): sys.exit()

amount = 0
for I in array:
    if I[1] == 'JPY': amount += int(I[0])
    if I[1] == 'BTC': amount += float(I[0]) * 380000

print(amount)