h = int(input())
w = int(input())
n = int(input())

print(n//max(h,w) if n%max(h,w)==0 else n//max(h,w)+1)