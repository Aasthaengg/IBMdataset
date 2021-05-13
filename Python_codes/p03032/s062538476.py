def main():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    m = 0
    for i in range(k+1):
        if i > n:
            rem = k-n
            have = v
            while len(have)>0 and have[0]<0 and rem>0:
                    have.pop(0)
                    rem -= 1
            s = sum(have)
            if m<s:
                m = s
            break
        for j in range(i+1):
            l=j
            r=i-l
            have = v[0:l]+v[n-r:n]
            rem = k-i
            have = sorted(have)
            if len(have)==0:
                s = 0
            else:
                while len(have)>0 and have[0]<0 and rem>0:
                    have.pop(0)
                    rem -= 1
                s = sum(have)
            if m<s:
                m = s
    print(m)

        

if __name__ == "__main__":
    main()