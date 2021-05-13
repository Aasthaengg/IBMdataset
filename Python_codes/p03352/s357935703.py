n = int(open(0).read().rstrip())

exes = {1}

for i in range(2,1001):
    if not i in exes:
        to_add = i
        while to_add * i <= 1000:
            to_add *= i
            exes.add(to_add)

print(max(filter(lambda x:x<=n, exes)))