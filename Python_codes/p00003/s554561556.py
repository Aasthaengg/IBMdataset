for i in range(int(raw_input())):
    n = sorted(map(int, raw_input().split()))
    print "YES" if n[2]**2 == n[1]**2 + n[0]**2 else "NO"