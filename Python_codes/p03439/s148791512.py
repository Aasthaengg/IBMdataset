n = int(input())
l, r = 0, n - 1
print(0)
data = input()
while data != "Vacant":
    m = (l + r) // 2
    print(m)
    s = input()
    if s == "Vacant":
        exit()
    if ( m % 2 == 0 and data == s) or ( m % 2 == 1 and data != s):
        l = m + 1
    else:
        r = m - 1
    
