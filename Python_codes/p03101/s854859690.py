h, w = [int(i) for i in input().split()]
h1, w1 = [int(i) for i in input().split()]
 
print(h * w - (h * w1 + w * h1 - h1 * w1))