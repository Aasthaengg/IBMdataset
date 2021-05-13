
def main():
    n = int(input())
    h=[int(i) for i in input().split()]
    min_h = min(h)
    h_sub = [int(i)-min_h for i in h]
    res = min_h
    i = 0
    while max(h_sub)!=0:
        if(h_sub[i]>0):
            res+=1
            j = i
            while(j<n and h_sub[j]!=0):
                h_sub[j]-=1
                j+=1
        else:
            i+=1
        if(i>=n):
            break
    print(res)

if __name__ == '__main__':
    main()
