n = int(input())
p = {'hon': {2, 4, 5, 7, 9}, 'pon': {0, 1, 6, 8}, 'bon': {3}}
for k, v in p.items():
    if n % 10 in v:
        print(k)