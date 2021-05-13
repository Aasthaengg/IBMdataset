def resolve():
    N = input().strip()
    carry = 0
    a = 0 # 99 -> 099
    b = 1 # 99 -> 100
    for ch in N:
        n = ord(ch) - ord('0')
        a2 = min(a+n, b+10-n)
        b = min(a+n+1, b+10-n-1)
        a=a2
    print(a)

resolve()