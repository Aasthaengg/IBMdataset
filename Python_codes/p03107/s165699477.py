s = input()
n = len(s)
red = sum([ 1 for i in s if i == '0' ])
blue = n - red
print(n-abs(red-blue))