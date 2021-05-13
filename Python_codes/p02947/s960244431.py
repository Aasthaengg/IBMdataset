from collections import Counter
print(sum([i*(i-1)//2 for i in [*Counter([''.join(sorted(input())) for _ in range(int(input()))]).values()]]))