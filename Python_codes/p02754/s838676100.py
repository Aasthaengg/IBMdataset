n,a,b = map(int, input().split())
ab = a+b
loop = n//ab
rem = n - loop*ab
blue = min(rem,a)
print(loop*a+blue)