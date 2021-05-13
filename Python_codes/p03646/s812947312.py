K = int(input())

core = [[49-i]*(50-i) + [50*2-i]*i for i in range(50)]

print(50)
print(' '.join([str(a+K//50) for a in core[K%50]]))
