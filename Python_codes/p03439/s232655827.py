import sys
n = int(input())
le = 0
ri = n
print(0)
sys.stdout.flush()
s = input()
if s == "Male":
    ls = "Male"
elif s == "Female":
    ls = "Female"
else:
    exit()

while ri > le + 1:
    m = (ri+le)//2
    print(m)
    sys.stdout.flush()
    s = input()
    if s == "Vacant":
        exit()
    if (m-le)%2:
        if s == ls:
            ri = m
        else:
            le = m
            ls = s
    else:
        if s == ls:
            le = m
            ls = s
        else:
            ri = m
print(le)
sys.stdout.flush()
exit()
