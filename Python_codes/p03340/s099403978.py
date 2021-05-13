def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = []
    q = 0
    ans_list = []
    x = a[0]
    s = a[0]
    for i in range(n):
        while True:
            if q == n-1:
                ans_list.append((i,q))
                break
            else:
                tx = x^a[q+1]
                ts = x+a[q+1]
                if tx != ts:
                    ans_list.append((i,q))
                    x ^= a[i]
                    s -= a[i]
                    if i == q:
                        q += 1
                        x = a[q]
                        y = a[q]
                    break
                else:
                    q += 1
                    x = tx
                    s = ts
    ans = 0
    for i in ans_list:
        ans += i[1]-i[0]+1
    print(ans)
    
if __name__ == '__main__':
    main()