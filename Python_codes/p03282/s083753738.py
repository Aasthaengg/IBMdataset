def main():
    s = input()
    k = int(input())
    r = '1'
    for i,v in enumerate(s):
        if v != '1':
            r = v
            break
    if i >= k:
        print(1)
    else:
        print(r)
    
if __name__ == "__main__":
    main()