N=int(input())
a=0
for i in range(1,36):a+=N//2//5**i
print(0 if N%2 else a)
