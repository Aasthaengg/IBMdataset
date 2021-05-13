def main():
    s = list(input())
    k = int(input())

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    D = dict(zip(ascii_lowercase,list(range(0,len(ascii_lowercase)))))

    n = len(ascii_lowercase)

    for i in range(0,len(s)):
        j = D[s[i]]
        if j != 0 and 26 -j <= k:
            k -= (26-j)
            s[i] ='a'

    if k >0:
        j = (D[s[-1]] + k%26)%26
        s[-1] = ascii_lowercase[j]
    print(''.join(s))

main()