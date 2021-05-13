def main():
    p, q, r = map(int, input().split())
    res = min(p + q, r + q, p + r)
    print(res)
    
if __name__ == '__main__':
    main()