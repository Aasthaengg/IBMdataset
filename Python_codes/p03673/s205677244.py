n=int(input())
a=input().split()
if n%2:
  print(" ".join(a[::-2]+a[1::2]))
else:
  print(" ".join(a[-1:0:-2]+a[::2]))
