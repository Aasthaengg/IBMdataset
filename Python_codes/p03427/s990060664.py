N = input()
k = int(N[0]) + 9*(len(N) - 1)
if N[1:] != '9' * (len(N) - 1):
    k -= 1     
print(k)