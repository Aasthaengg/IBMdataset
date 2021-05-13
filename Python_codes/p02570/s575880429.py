# coding: utf-8
def main():
	d,t,s = map(int, input().split())
	if t-(d/s) >= 0:
		print('Yes')
	else:
		print('No')


if __name__ == '__main__':
	main()
