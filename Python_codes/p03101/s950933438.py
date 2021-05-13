l = input().split(" ")
s = input().split(" ")

H = int(l[0])
W = int(l[1])
h = int(s[0])
w = int(s[1])

print(H*W-(w*H + h*W - w*h))