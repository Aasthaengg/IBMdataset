def main():
    n=int(input())
    h=list(map(int,input().split()))
    count = 0
    while max(h) > 0:
        m = 101
        i = 0
        while h[i] == 0:
            i += 1
        j = i
        while i < n:
            if j == n or h[j] == 0:
                count += m
                for x in range(i,j):
                    h[x] -= m
                i = j
                break
            elif h[j] != 0:
                m = min(m, h[j])
            j += 1
    print(count)
    
if __name__ == "__main__":
    main()