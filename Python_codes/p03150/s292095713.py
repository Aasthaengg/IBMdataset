def main():
    s = input()
    n = len(s)
    
    for i in range(n):
        for j in range(i,n):
            if s[:i]+s[j:]=='keyence':
                return 'YES'
    return 'NO'
print(main())