k = int(input())

q, mod = divmod(k, 50)
l = [50 if mod > 0 and i == (50-mod) else i for i in range(50)]

result = [str(q+l[i]) for i in range(50)]
print(50)
print(" ".join(result))
