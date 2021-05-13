n = int(input())
h = int(n/(60*60))
n -= h*(60*60)
m = int(n/(60))
n -= m*60
print("{}:{}:{}".format(h, m, n))