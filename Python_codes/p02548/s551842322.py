n = int(input()) - 1
lst = [n // k for k in range(1, int(n**0.5+1))]
print(2 * sum(lst) - int(n**0.5)**2)
