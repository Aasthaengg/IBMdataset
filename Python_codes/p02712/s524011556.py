N = int(input())
res = (N * (N + 1)) / 2
three = ( (3 + 3 * (N // 3)) * (N // 3) )/ 2
five =  ( (5 + 5 * (N // 5)) * (N // 5) )/ 2
threefive =  ( (15 + 15 * (N // 15)) * (N // 15) )/ 2
print(int(res - three - five + threefive))