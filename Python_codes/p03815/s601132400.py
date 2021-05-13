X = int(input())

q, r = divmod(X, 11)

if r == 0:
    output = q * 2
elif r <= 6 :
    output = q * 2 + 1
else :
    output = q * 2 + 2

print(output)
