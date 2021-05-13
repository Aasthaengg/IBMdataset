n, a, b = map(int, input().split())
population_max = a
if b < a:
    population_max = b
population_min = 0
if a+b > n:
    population_min = (a+b)-n
print('{0} {1}'.format(population_max, population_min))
