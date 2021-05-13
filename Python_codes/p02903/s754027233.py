import numpy
h, w, a, b = map(int,input().split())
s = numpy.zeros([h,w],int)
for i in range(h):
    ans = []
    for j in range(w):
        if i < b and j < a:
            ans.append("1")
        elif i < b and a <= j:
            ans.append("0")
        elif b <= i and j < a:
            ans.append("0")
        else:
            ans.append("1")
    print("".join(ans))




