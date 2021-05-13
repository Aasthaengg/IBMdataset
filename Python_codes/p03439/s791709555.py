n = int(input())
print(0)
l = input()
if l == "Vacant":
    exit()
print(n-1)
r = input()
if r == "Vacant":
    exit()
s = "none"
l_n = 0
r_n = n-1
while True:
    s_n = (l_n+r_n)//2
    print(s_n)
    diff = s_n - l_n
    s = input()
    if s == "Vacant":
        exit()
    elif s == "Male" and diff % 2 == 0:
        if l == "Male":
            l_n = s_n
        else:
            r = "Male"
            r_n = s_n
    elif s == "Male" and diff % 2 == 1:
        if l == "Male":
            r = "Male"
            r_n = s_n
        else:
            l = "Male"
            l_n = s_n
    elif s == "Female" and diff % 2 == 0:
        if l == "Female":
            l_n = s_n
        else:
            r = "Female"
            r_n = s_n
    elif s == "Female" and diff % 2 == 1:
        if l == "Female":
            r = "Female"
            r_n = s_n
        else:
            l = "Female"
            l_n = s_n

