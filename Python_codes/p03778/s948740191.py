# such silly mistakes i am noob
w, a, b = map(int , input().split())
if b>=a and b<=w+a:
	print(0)
elif b+w>=a and b+w<=a+w:
	print(0)
elif b+w<a:
	print(a-(b+w))
elif a+w<b:
	print(b-(a+w))