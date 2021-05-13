def main():
    n = int(input())
    i = 0
    d = {"Vacant": 2, "Male": 0, "Female": 1}
    print(i)
    s = d[input()]
    if s == 2:
        return 0
    lower = 0
    upper = n - 1
    while True:
        mid=lower+(upper-lower)//2
        print(mid)
        s2 = d[input()]
        if s2 == 2:
            return 0
        if mid > i:
            if abs(mid - i) % 2 == (s != s2):
                lower = mid+1
            else:
                upper = mid
        else:
            if abs(mid - i) % 2 == (s != s2):
                upper = mid
            else:
                lower = mid+1
        i = mid
        s=s2
main()