def even(num):
	return num//2

def odd(num):
	return num//2+num%2


K=int(input())

print(even(K)*odd(K))