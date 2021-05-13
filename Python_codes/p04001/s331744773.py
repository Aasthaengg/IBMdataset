def main():
    a = input()
    p = len(a)
    ans =0
    for i in range(2**(p-1)):
        t =a[0]
        for j in range(p-1):
            if (i & 1 <<j):
                t = t + '+'
            t = t + a[j+1]
        ans += eval(t)
    print(ans)
if __name__ =='__main__':
    main()