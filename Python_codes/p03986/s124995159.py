# A - STring

X = input()
count = max_count = 0
ST = {'S':-1, 'T':1}

for i in range(len(X)):
    count += ST[X[i]]
    if count > max_count:
        max_count = count

print(2*max_count)