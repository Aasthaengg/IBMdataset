n = int(input())

for i in range((10**9)+1):
    if i**2 > n:
        print((i-1)**2)
        break
