

def main():
    d = int(input())
    c = [0] + list(map(int,input().split()))
    last = [0] * 27
    s = [0]
    for i in range(d):
        s.append([0] + list(map(int,input().split())))
    total = 0
    for j in range(1,d+1):
        t = int(input())
        last[t] = j
        total += s[j][t]
        for k in range(1,27):
            total -= c[k] * (j - last[k])
        print(total)






if __name__ == '__main__':
    main()
