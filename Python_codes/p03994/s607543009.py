def main():
    s = list(input())
    k = int(input())

    for i in range(len(s)-1):
        if s[i] == 'a':
            continue
        else:
            mod = 26-(ord(s[i])-97)%26
            if k >= mod:
                k -= mod
                s[i] = 'a'
            if k == 0:
                break
    
    if k > 0:
        mod = ((ord(s[-1])-97)+k)%26
        s[-1] = chr(mod+97)
    print(''.join(s))

if __name__ == '__main__':
    main()

