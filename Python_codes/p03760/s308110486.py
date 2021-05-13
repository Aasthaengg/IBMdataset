import itertools as it
print("".join(it.chain.from_iterable(it.zip_longest(*[input() for _ in range(2)],fillvalue=""))))