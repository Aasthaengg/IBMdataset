def main():
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff_0 = a[0]-b[0]
    diff_1 = a[1]-b[1]

    if diff_0*diff_1 > 0:
        return 0
    
    d_one_iter = diff_0*t[0]+diff_1*t[1]

    if diff_0*d_one_iter > 0:
        return 0
    if diff_0*d_one_iter == 0:
        return 'infinity'
    
    if abs(diff_0*t[0])%abs(d_one_iter) == 0:
        return 2*abs(diff_0*t[0])//abs(d_one_iter)
    else:
        return 2*(abs(diff_0*t[0])//abs(d_one_iter))+1

if __name__ == "__main__":
    print(main())