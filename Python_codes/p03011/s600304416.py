def main():
    p,q,r = map(int, input().split())
    min_time = min([p+q, q+r, r+p])
    print(min_time)

if __name__ == '__main__':
	main()