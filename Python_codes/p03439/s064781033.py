import sys
n = int(input())
D = {}
for i in [0,n-1]:
    print(i,flush=True)
    s = input()
    if s == "Vacant":
        sys.exit()
    D[i] = s
inf = 0
sup = n
while True:
    mid = (sup+inf)//2
    print(mid,flush=True)
    s = input()
    if s == "Vacant":
        sys.exit()
    else:
        D[mid] = s
        if ((mid%2==inf%2) != (D[mid] == D[inf])):
            sup = mid
        else:
            inf = mid